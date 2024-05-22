"""Moduel for metrics of country data"""

class DispersionMetrics:
    """
    A class to represent a country's cultural dimensions.
    """
    pdi: int  # power distance
    idv : int  # individualism
    mas : int  # masculinity
    uai : int  # uncertainity
    lto: int  # long term orientation
    ind: int   # indulgence

    def __init__(self, culture_data: dict):
        """
        Constructs all the necessary attributes for the country object.

        Parameters:
        culture_data (dict): A dictionary containing the country's name, code, and cultural dimensions.
                            dict keys: 'name (str)', 'code (str)', 'pdi (int)', 'idv (int)', 'mas (int)', 'uai (int)', 'lto (int)', 'ind (int)'
        """
        self.pdi = culture_data['pdi']
        self.idv = culture_data['idv']
        self.mas = culture_data['mas']
        self.uai = culture_data['uai']
        self.lto = culture_data['lto']
        self.ind = culture_data['ind']
    
    def __str__(self):
        return f'PDI: {self.pdi}, IDV: {self.idv}, MAS: {self.mas}, UAI: {self.uai}, LTO: {self.lto}, IND: {self.ind}'

class PowerDistance:
    """
    pdi value è il valore della deviazione standard
    """
    def __init__(self, pdiValue):
        self.PDIValue = pdiValue
        self.PDIDescription = "PDI expresses the degree to which the less powerful members of a society accept and expect that power is distributed unequally. People in societies exhibiting a high level of Power Distance accept a hierarchical order in which everybody has a determined place. On the contrary, in societies with low Power Distance, people strive to equalize the distribution of power and demand justification for power inequalities."
        self.PDIDispersionDescription = ""
        self.PDIDispersionEffects = []

        if self.PDIValue < 25:
            self.PDIDispersionDescription = "Your community exhibits low dispersion values for this index. This could indicate that most of its members share similar views on how power should be distributed."
        else:
            self.PDIDispersionDescription = "Your community exhibits a high value for this index. This could indicate that there is no common vision on how power should be distributed. Such a situation might lead some members of the community to be dissatisfied with the way decisions are made."
            self.PDIDispersionEffects.append(
                "Such dispersion has been correlated with the emergence of the radio silence effect, i.e., a situation where the project is damaged because information exchange does not reach all members of the group but occurs only through a few individuals. This can lead to communication overhead and information loss. In dispersed communities, this situation can lead to dissatisfaction among individuals who would prefer a more equitable distribution of power.")

    def toDict(self):
        return {
            "metric_name:": "Power Distance",
            "description:": self.PDIDescription,
            "effects": self.PDIDispersionEffects,
            "dispersion_value": self.PDIValue,
            "dispersion_description": self.PDIDispersionDescription
        }

class Individualism:
    def __init__(self, idvDispersion):
        self.IDVDispersionValue = idvDispersion
        self.IDVDescription = "Your community exhibits a low dispersion value for this index. This could indicate that most of its members share the same preference regarding working in groups or alone."
        self.IDVDispersionDescription = ""
        self.IDVDispersionEffects = []

        if idvDispersion < 25:
            self.IDVDispersionDescription = "Your community exhibits a low dispersion value for this index. This could indicate that most of its members share the same preference regarding working in groups or alone."
            self.IDVDispersionEffects.append("Research has demonstrated a correlation between such dispersion and the emergence of radio silence, i.e., a situation where the project is damaged because information exchange does not reach all members of the group but occurs only through a few individuals. This can be explained by the fact that in communities where most individuals have an individualistic approach, there tends to be less information exchange and a preference for a situation where a single individual handles communication. This situation (particularly in geographically distributed teams) can lead to communication overhead and information loss.")
        else:
            self.IDVDispersionDescription = "Your community exhibits a high dispersion value for this index. This could indicate that your community is composed of both collectivists and individualists, with the consequent risk of conflicts arising during work."
            self.IDVDispersionEffects.append("The cultural dispersion of Individualism vs Collectivism has been correlated with the emergence of the Lone Wolf phenomenon, a situation where a member of the community starts acting alone and without communicating, consequently damaging the information exchange within the project. This is understandable given that having many individuals who prefer to work in groups alongside others who prefer to work alone can exacerbate the occurrence of developer isolation.")
            self.IDVDispersionEffects.append("Research has demonstrated a correlation between such dispersion and the emergence of radio silence, i.e., a situation where the project is damaged because information exchange does not reach all members of the group but occurs only through a few individuals. This can be explained by the fact that in communities without a unified vision, some individuals tend to impose themselves as the sole communication points. This can lead to information loss and conflict, especially if collectivists feel excluded.")

    def toDict(self):
        return {
            "metric_name:": "Individualism",
            "description:": self.IDVDescription,
            "effects": self.IDVDispersionEffects,
            "dispersion_value": self.IDVDispersionValue,
            "dispersion_description": self.IDVDispersionDescription
        }


class Masculinity:
    def __init__(self, MASDispersion):
        self.MASDescription = "MAS represents a contrast between two preferences. The Masculinity side (high level) is defined as 'a preference in society for achievement, heroism, assertiveness and material rewards for success'. In contrast, the Femininity side (low level) represents 'a preference for cooperation, caring for the weak and quality of life'."
        self.MASDispersionDescription = ""
        self.MASDispersionEffects = []
        self.MASDispersion = MASDispersion

        if self.MASDispersion < 25:
            self.MASDispersionDescription = "Your community exhibits a low dispersion value for this index. This could indicate that the members of your community share the same view on what is more important: prevailing over others or creating a social and non-competitive environment."
        else:
            self.MASDispersionDescription = "Your community exhibits a high dispersion value for this index. This could indicate that the members of your community have different views on what is more important: prevailing over others or creating a social and non-competitive environment."

    def toDict(self):
        return {
            "metric_name:": "Masculinity",
            "description:": self.MASDescription,
            "effects": self.MASDispersionEffects,
            "dispersion_value": self.MASDispersion,
            "dispersion_description": self.MASDispersionDescription
        }


class Uncertainty:
    def __init__(self, UAIDispersion):
        self.UAIDescription = "UAI expresses the degree to which the members of a society feel uncomfortable with uncertainty and ambiguity. Countries exhibiting high level of UAI maintain rigid codes of belief and behavior and are intolerant of unorthodox behavior and ideas. Conversely, a low level of UAI indicates societies that maintain a more relaxed attitude in which practice counts more than principles."
        self.UAIDispersionDescription = ""
        self.UAIDispersionEffects = []
        self.UAIDispersion = UAIDispersion

        if UAIDispersion < 25:
            self.UAIDispersionDescription = "Your community exhibits a low dispersion value for this index. This could indicate that the individuals in your community have the same level of risk tolerance (either low or high)."
        else:
            self.UAIDispersionDescription = "Your community exhibits a high dispersion value for this index. This could indicate that your community includes both individuals who feel comfortable trying new things and those who prefer to stick with well-known technologies."

    def toDict(self):
        return {
            "metric_name:": "Uncertainity",
            "description:": self.UAIDescription,
            "effects": self.UAIDispersionEffects,
            "dispersion_value": self.UAIDispersion,
            "dispersion_description": self.UAIDispersionDescription
        }

class LongTermOrientation:
    def __init__(self, ltoDispersion):
        self.LTODescription = "LTO measures how much people are oriented toward a long-term outlook in contrast to a more short-term. A high degree in this index (Long-Term) indicates that people encourage thrift and efforts in modern education as a way to prepare for the future. On the contrary, a lower degree of this index (Short-Term) indicates that people tend to honor traditions and value steadfastness."
        self.LTODispersionDescription = ""
        self.LTODispersionEffects = []
        self.LTODispersionValue = ltoDispersion

        if self.LTODispersionValue < 25:
            self.LTODispersionDescription = "Your community exhibits a low dispersion value for this index. This could indicate that your community shares the same perspective on how the team's vision should be set (whether long-term or short-term)."
        else:
            self.LTODispersionDescription = "Your community exhibits a high dispersion value for this index. This could indicate that your community includes both individuals who prefer achieving short-term results and those who prefer investing for greater long-term benefits."

    def toDict(self):
        return {
            "metric_name:": "Long term Orientation",
            "description:": self.LTODescription,
            "effects": self.LTODispersionEffects,
            "dispersion_value": self.LTODispersionValue,
            "dispersion_description": self.LTODispersionDescription
        }

class Indulgence:
    def __init__(self, IndulgenceDispersion):
        self.IVRDescription = "IVR refers to the degree of freedom that societal norms give citizens to fulfill their human desires. A high level (Indulgence) indicates a society that allows relatively free gratification of basic and natural human desires related to enjoying life and having fun. Conversely, a low level (Restraint) indicates a society that controls gratification of needs and regulates it using strict social norms."
        self.IVRDispersionDescription = ""
        self.IVRDispersionEffects = []
        self.IVRDispersion = IndulgenceDispersion

        if self.IVRDispersion < 25:
            self.IVRDispersionDescription = "Your community exhibits a low dispersion value for this index. This could indicate that individuals share the same view on how much the state or organizations should support individuals in leisure activities rather than work activities."
        else:
            self.IVRDispersionDescription = "Your community exhibits a high dispersion value for this index. This could indicate that individuals do not share the same view on how much the state or organizations should support individuals in leisure activities rather than work activities. This situation might require greater flexibility in how the company approaches employees' leisure time."

    def toDict(self):
        return {
            "metric_name:": "Indulgence",
            "description:": self.IVRDescription,
            "effects": self.IVRDispersionEffects,
            "dispersion_value": self.IVRDispersion,
            "dispersion_description": self.IVRDispersionDescription
        }
class GeographicalDispersion:
    def __init__(self, geographicalDispersionValue):
        self.geoDispersionDescription = "Geographical Dispersion is a measure of how the members of a community are distributed around the globe and distant from each other."
        self.geoDispersionEffects = []
        self.geoDispersionValue = geographicalDispersionValue

        if geographicalDispersionValue >= 75:
            self.geoDispersionEffects.append("Geographical dispersion has been correlated with the emergence of Black Cloud. This could be due to the fact that in geographically distributed communities, where most members work in different parts of the globe, there are fewer opportunities for information exchange (including informal exchanges) compared to communities in the same location.")
            self.geoDispersionEffects.append("Geographical dispersion has been correlated with the emergence of Organizational Silos. This could be due to the fact that in geographically distributed communities, where most members work in different parts of the globe, coordinating tasks among them and ensuring these tasks are interconnected can be challenging.")
            self.geoDispersionEffects.append("Geographical dispersion has been correlated with the emergence of Radio Silence. This could be due to the fact that in geographically distributed communities, where most members work in different parts of the globe, it is more common for individual members to manage communication between different groups. However, this can lead to communication overhead and, consequently, a loss of information.")

    def toDict(self):
        return {
            "metric_name:": "Geographical dispersion",
            "description:": self.geoDispersionDescription,
            "effects": self.geoDispersionEffects,
            "value": self.geoDispersionValue
        }