# turn-image-to-ascii
takes a provided image and makes a .txt file with the image drawn in ascii characters

# examples: 
## original image:
![mario](https://user-images.githubusercontent.com/51734410/196738211-15f0d688-c5a6-40a2-bbba-a215015df8c6.jpg) 

## basic ascii table:
![sdads](https://user-images.githubusercontent.com/51734410/201487634-07263280-5eec-4707-a923-d104ce368679.png)

## flat ascii table:
![Screenshot_20221112_194833](https://user-images.githubusercontent.com/51734410/201487663-a5e3b54d-5971-46f0-ad84-5e1bac0c4f18.png)

## dependencies:
you need pillow which comes with python 3 as far as im aware but it gave me problems so if it does it to you try running the install command again (this is for linux):

```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

## how to use:
first type ``` chmod +x imageToAscii ``` to the file, you can just use python3 to run it but this is more comfotrable
then type the following command into the terminal and you get a file as an output:
```
imageToAscii size_of_ascii_image /optional_path_to_file/name_of_file /optional_path_to_file/name_of_output_file
```

### side note:
while this *technically* works on windows it dosent draw the image correctly and for now i cant fix it, but hopefuly you can fix it

tested on:
fedora 36, android.
