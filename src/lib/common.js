// common functions

export const fmtFieldsList = (fieldsObj) => {
  // returns fields and relationships
  const fields = []
  const relations = []
  for (var name in fieldsObj) {
    var fmtField = { name: name, ...fieldsObj[name] }
    if (fmtField.relationship === undefined) {
      fields.push(fmtField)
    } else {
      relations.push(fmtField)
    }
  }
  return { fields: fields, relations: relations }
}

export const showRequirements = (requirements) => {
  if (requirements === undefined) {
    return '(Any requirements from method decorators would show here.)'
  } else {
    return requirements
  }
}
