Repository: RVC-Boss/GPT-SoVITS
Language: Python
Stars: 47839
Forks: 5265
-----
Use the command line to open the WebUI for UVR5  
```bash
python tools/uvr5/webui.py "<infer_device>" <is_half> <webui_port_uvr5>
```  
<!-- If you can't open a browser, follow the format below for UVR processing,This is using mdxnet for audio processing
```
python mdxnet.py --model --input_root --output_vocal --output_ins --agg_level --format --device --is_half_precision
``` -->  
This is how the audio segmentation of the dataset is done using the command line  
```bash
python audio_slicer.py \
--input_path "<path_to_original_audio_file_or_directory>" \
--output_root "<directory_where_subdivided_audio_clips_will_be_saved>" \
--threshold <volume_threshold> \
--min_length <minimum_duration_of_each_subclip> \
--min_interval <shortest_time_gap_between_adjacent_subclips>
--hop_size <step_size_for_computing_volume_curve>
```  
This is how dataset ASR processing is done using the command line(Only Chinese)  
```bash
python tools/asr/funasr_asr.py -i <input> -o <output>
```  
ASR processing is performed through Faster_Whisper(ASR marking except Chinese)  
(No progress bars, GPU performance may cause time delays)  
```bash
python ./tools/asr/fasterwhisper_asr.py -i <input> -o <output> -l <language> -p <precision>
```  
A custom list save path is enabled