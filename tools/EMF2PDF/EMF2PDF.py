

def convert_EMF_to_PDF(self, infile, outfile):

        path_infile = self.dataDir + infile
        path_outfile = self.dataDir + outfile

        (w, h) = self.helper.get_image_size(path_infile)

        # Initialize new Document

        document = Document()
        page = document.Pages.Add()
        image = Image()
        image.File = path_infile

        # Set page dimensions

        page.PageInfo.Height = h
        page.PageInfo.Width = w
        page.PageInfo.Margin.Bottom = 0
        page.PageInfo.Margin.Top = 0
        page.PageInfo.Margin.Right = 0
        page.PageInfo.Margin.Left = 0
        page.Paragraphs.Add(image)

        # Save the file into PDF format

        document.Save(path_outfile)
        print(infile + " converted into " + outfile)
