<h1>blankspace</h1>

<h3>UNC4990 obfuscation technique to hide payloads in a "blank" text file</h3>

I recently saw an article from Mandiant that covered this technique used by UNC4990 on which it sparked my interest to develop a script that obfuscate and deobfuscate based from this technique. Can be useful for red team engagements or if you encountered a "blank" text file that appears to be suspicious, you can use the decoding script to see the deobfuscated version.

![image](https://github.com/sscoconutree/blankspace/assets/59388557/7ed2b9d6-e97a-49ae-96a0-9f2336168044)

Reference: https://www.mandiant.com/resources/blog/unc4990-evolution-usb-malware

⚠️ Disclaimer: Employing the methods and principles outlined in this repository to obtain unauthorized entry into systems without proper authorization is against the law. You are accountable for your conduct. Act responsibly and refrain from engaging in malicious activities. This is for educational purposes only.

<h2>Instructions: cantseeme.py</h2>

This script is to encode a text file from its ASCII format to "spaces" and "tabs".

1. Below is a sample text file that contains an obfuscated version of a reverse shell.

![image](https://github.com/sscoconutree/blankspace/assets/59388557/2d1da9aa-cd42-4d82-b6b9-bd04fa9c0ffb)

2. Use the script to convert the file from its ASCII format to "spaces" and "tabs".

![image](https://github.com/sscoconutree/blankspace/assets/59388557/10c76ddf-0a58-4d9b-8612-fa5d812ff297)

3. Checking the output file, the reverse shell appears to be hidden as "spaces" and "tabs".

![image](https://github.com/sscoconutree/blankspace/assets/59388557/3dee491e-e6a9-4ac6-ab0d-de0cddbda8b1)

![image](https://github.com/sscoconutree/blankspace/assets/59388557/49ff7d0d-56ba-4d2a-a6e7-ba2355316368)

<h2>Instructions: iseeyou.py</h2>

This script is to decode a text file that contains "tabs" and "spaces" back to its ASCII format.

1. Below is a sample "blank" text file that contains "tabs" and "spaces".

![image](https://github.com/sscoconutree/blankspace/assets/59388557/6c518ba7-d0ab-40df-b891-10e8de3d5138)

2. Use the script to decode the "blank" text file back to its ASCII format.

![image](https://github.com/sscoconutree/blankspace/assets/59388557/11bd0877-aaaf-42c8-9236-0977a6783de7)



