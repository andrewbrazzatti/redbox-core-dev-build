import time
from org.apache.commons.lang import StringEscapeUtils

class DatasetData:
    def __activate__(self, context):
        self.formData = context["formData"]

    def getFormData(self, field):
        return StringEscapeUtils.escapeHtml(self.formData.get(field, ""))

    def getCurrentTime(self):
        return time.strftime("%Y-%m-%dT%H:%M:%SZ")

    def getCleanId(self, id):
        return id.replace(":","").replace(".","")
