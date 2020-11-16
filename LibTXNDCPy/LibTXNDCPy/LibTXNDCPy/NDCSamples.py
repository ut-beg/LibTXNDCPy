import NDCSample
import NGGDPPTypes
from io import StringIO

class NDCSamples(object):
    """description of class"""

    def __init__(self):
        self._samples = []

    @property
    def samples(self):
        return self._samples

    def createSample(self):
        sample = NDCSample.NDCSample()
        return sample

    def addSample(self, sample):
        if sample not in self.samples:
            self.samples.append(sample)

    def removeSample(self, sample):
        if sample in self.samples:
            self.samples.remove(sample)

    def toNDCXml(self):
        ret = NGGDPPTypes.samples()

        for samp in self.samples:
            sampX = samp.toNDCXml()
            ret.add_sample(sampX)

        return ret

    def toNDCXmlString(self):
        ret = ""

        xmlObj = self.toNDCXml()

        sio = StringIO("")

        xmlObj.export(sio, 0)

        ret = sio.getvalue()

        return ret

    def initWithJson(json): 
        for jsample in json["samples"]:
            sample = NDCSample()

            sample.initWithJson(jsample)

            self.addSample(sample)
            