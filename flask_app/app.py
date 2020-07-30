# examples/invoice_app.py
"""
This app provides an example posting child relations with a
parent class through the example of an invoice.

"""
# initialize
from os import path
from flask import Flask
from flask_cors import CORS

from flask_restful import Api, Resource
from flask_restful_dbbase import DBBase
from flask_restful_dbbase.resources import (
    CollectionModelResource,
    ModelResource,
    MetaResource,
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)
db = DBBase(app)
CORS(app)

URL_PREFIX = "/api/v1"
all_metas = {}


def add_meta(meta_resource):
    """
    all_metas are keyed by res_endpoint.
    format:
    {
        res_endpoint: {
            meta_url: meta_resource.get_urls()[0]
            resource_urls: resource.get_urls()
        }
    }

    """
    resource = meta_resource.resource_class
    cls = resource.model_class
    res_endpoint = resource.__name__
    print("res_endpoint", res_endpoint)
    all_metas[res_endpoint] = {
        "name": res_endpoint,
        "metaUrl": meta_resource.get_urls()[0],
        "resourceUrls": resource.get_urls(),
    }


# define invoice
class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, nullable=True, primary_key=True)
    name = db.Column(db.String, nullable=False)

    invoices = db.relationship("Invoice", backref="customer")


class Invoice(db.Model):
    __tablename__ = "invoice"

    id = db.Column(db.Integer, nullable=True, primary_key=True)
    customer_id = db.Column(
        db.Integer, db.ForeignKey("customer.id"), nullable=False
    )
    invoice_date = db.Column(db.Date, nullable=False)

    invoice_items = db.relationship("InvoiceItem", backref="invoice")


class InvoiceItem(db.Model):
    __tablename__ = "invoice_item"

    id = db.Column(db.Integer, nullable=True, primary_key=True)
    invoice_id = db.Column(
        db.Integer, db.ForeignKey("invoice.id"), nullable=False
    )
    part_code = db.Column(db.String, nullable=False)
    units = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float(precision=2), nullable=False)


db.create_all()


class CustomerResource(ModelResource):
    model_class = Customer
    url_prefix = URL_PREFIX


class CustomerCollectionResource(CollectionModelResource):
    model_class = Customer
    url_prefix = URL_PREFIX


class InvoiceResource(ModelResource):
    model_class = Invoice
    url_prefix = URL_PREFIX

    # necessary only if the database does not understand
    #   dates in string form -- such as Sqlite3
    use_date_conversions = True


class InvoiceCollectionResource(CollectionModelResource):
    model_class = Invoice
    url_prefix = URL_PREFIX


class InvoiceItemResource(ModelResource):
    model_class = InvoiceItem
    url_prefix = URL_PREFIX


class InvoiceItemCollectionResource(ModelResource):
    model_class = InvoiceItem
    url_prefix = URL_PREFIX


# create meta resources
# NOTE: url_prefix for meta resources derive from the resource_class
#       so unnecessary to add explicitly
class CustomerMeta(MetaResource):
    resource_class = CustomerResource


class CustomerCollectionMeta(MetaResource):
    resource_class = CustomerCollectionResource


class InvoiceMeta(MetaResource):
    resource_class = InvoiceResource


class InvoiceCollectionMeta(MetaResource):
    resource_class = InvoiceCollectionResource


class InvoiceItemMeta(MetaResource):
    resource_class = InvoiceItemResource


class InvoiceItemCollectionMeta(MetaResource):
    resource_class = InvoiceItemCollectionResource


# add the resources to the API
api.add_resource(
    CustomerCollectionResource, *CustomerCollectionResource.get_urls()
)
api.add_resource(CustomerResource, *CustomerResource.get_urls())

api.add_resource(
    InvoiceCollectionResource, *InvoiceCollectionResource.get_urls()
)
api.add_resource(InvoiceResource, *InvoiceResource.get_urls())
api.add_resource(
    InvoiceItemCollectionResource, *InvoiceItemCollectionResource.get_urls()
)
api.add_resource(InvoiceItemResource, *InvoiceResource.get_urls())

api.add_resource(CustomerCollectionMeta, *CustomerCollectionMeta.get_urls())
api.add_resource(CustomerMeta, *CustomerMeta.get_urls())
api.add_resource(InvoiceMeta, *InvoiceMeta.get_urls())
api.add_resource(InvoiceCollectionMeta, *InvoiceCollectionMeta.get_urls())
api.add_resource(InvoiceItemMeta, *InvoiceItemMeta.get_urls())
api.add_resource(
    InvoiceItemCollectionMeta, *InvoiceItemCollectionMeta.get_urls()
)

# all classes meta
class MetaClassCollectionResource(Resource):
    url_prefix = URL_PREFIX
    url_name = "meta/classes"

    @classmethod
    def get_urls(cls):
        """This is to maintain consistency with the other resources."""
        return [path.join(cls.url_prefix, cls.url_name)]

    def get(self):

        class_list = sorted(
            [
                cls
                for cls in db.Model._decl_class_registry.keys()
                if not cls.startswith("_")
            ]
        )
        return {"classes": class_list}, 200


class MetaClassResource(Resource):
    url_prefix = URL_PREFIX
    url_name = "meta/classes/<string:name>"

    @classmethod
    def get_urls(cls):
        """This is to maintain consistency with the other resources."""
        return [path.join(cls.url_prefix, cls.url_name)]

    def get(self, **kwargs):
        name = kwargs.get("name", None)
        try:
            cls = db.Model._decl_class_registry[name]
            return db.doc_table(cls, to_camel_case=True), 200
        except:
            return (
                {
                    "message": f"Invalid class name: {name}. Names are case "
                    "sensitive, by the way"
                },
                400,
            )


api.add_resource(
    MetaClassCollectionResource, *MetaClassCollectionResource.get_urls()
)
api.add_resource(MetaClassResource, *MetaClassResource.get_urls())

all_meta_resources = [
    CustomerCollectionMeta,
    CustomerMeta,
    InvoiceMeta,
    InvoiceCollectionMeta,
    InvoiceItemMeta,
    InvoiceItemCollectionMeta,
    # MetaClassCollectionResource,
    # MetaClassResource,
]

for meta_resource in all_meta_resources:
    add_meta(meta_resource)


# notice that this a plain resource
class AllMetaUrlsResource(Resource):
    def get(self, **kwargs):
        return {"resources": all_metas}, 200


meta_url = path.join(URL_PREFIX, "meta")
api.add_resource(AllMetaUrlsResource, meta_url)


# URLs
ulist = []

ulist.extend(CustomerCollectionResource.get_urls())
ulist.extend(CustomerResource.get_urls())

ulist.extend(InvoiceCollectionResource.get_urls())

ulist.extend(InvoiceResource.get_urls())
ulist.extend(InvoiceItemCollectionResource.get_urls())
ulist.extend(InvoiceResource.get_urls())

ulist.extend(CustomerCollectionMeta.get_urls())
ulist.extend(CustomerMeta.get_urls())
ulist.extend(InvoiceMeta.get_urls())
ulist.extend(InvoiceCollectionMeta.get_urls())
ulist.extend(InvoiceItemMeta.get_urls())
ulist.extend(InvoiceItemCollectionMeta.get_urls())
ulist.extend(MetaClassCollectionResource.get_urls())
ulist.extend(MetaClassResource.get_urls())
ulist.append(meta_url)

urls = set(ulist)
print()
print("\n".join(sorted(urls)))
print()
if __name__ == "__main__":
    app.run(debug=True)
