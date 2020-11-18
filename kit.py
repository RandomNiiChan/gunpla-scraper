class Kit : 

    def __init__(
        self, 
        id, 
        model, 
        series, 
        release_year, 
        notes, 
        imageLink, 
        grade, 
        scale, 
        pbandai,
        variation
    ):
        self.grade = grade
        self.model = model
        self.series = series
        self.releaseYear = release_year
        self.notes = notes
        self.imageLink = imageLink
        self.scale = scale
        self.pbandai = pbandai
        self.id = id
        self.variation = variation
        
    def json(self):
        root = {
            "id":self.id,
            "grade":self.grade,
            "release_year":self.releaseYear,
            "name":self.model,
            "p-bandai":self.pbandai,
            "info":{
                "scale":self.scale,
                "series":self.series,
                "notes":self.notes
            }
        }
        link = [self.imageLink] if self.imageLink != None else []
        root["info"]["image_link"] = link
        if self.variation != None :
            root["variation"] = self.variation
        return root