# Analyzer topic and sentiment of news

To speed up the launch of the test and the application, you need to run:
1) download files at this [link](https://drive.google.com/drive/folders/1O0irJUvQdBF6jBSKk7qMbEFe_I3qdVTF?usp=drive_link);
2) put sent_model in the sentiment_serivce folder, and class_model in the classification_service folder;
3) change the source of models via variable "pt_save_directory" from the comment;
4) change the timer to unit_test.sh.

The main service is available at http://localhost:8001/analysis/, it takes the query parameter "text".

Automatic run instructions:
```bash
# Run app
run_app.sh

# Unit tests
unit_test.sh
```
