from arcgis.learn import prepare_data, FasterRCNN

def load_model(model_path):
    return FasterRCNN.from_model(model_path)

def predict_on_video(model, video_file, metadata_file, threshold=0.8):
    model.predict_video(input_video_path=video_file,
                        metadata_file=metadata_file,
                        track=True,
                        threshold=threshold,
                        visualize=True,
                        resize=True)

def main():
    model_path = r'C:/Users/jv_at/tcc/Arcgis/Amostra_total/models/model_faster50_2_Vehicle'
    video_file = r'C:\Users\jv_at\tcc\Arcgis\lev_7h_1_A1_estabilizado.mp4'
    metadata_file = 'lev_7h_1_A1.csv'

    model = load_model(model_path)
    predict_on_video(model, video_file, metadata_file)

if __name__ == '__main__':
    main()
