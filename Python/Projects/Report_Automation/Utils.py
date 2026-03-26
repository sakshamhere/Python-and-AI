

def replace_with_app_data(report,document):
    app_data = dict(report.app_data)
    for para in document.paragraphs:
        for key in app_data:
            if key in para.text:
                inline = para.runs
                for i in range(len(inline)):
                    if key in inline[i].text:
                        text = inline[i].text.replace(key,str(app_data[key]))
                        inline[i].text = text

    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    for key, value in app_data.items():
                        if key in para.text:
                            for run in para.runs:
                                if key in run.text:
                                    run.text = run.text.replace(key, str(value))
