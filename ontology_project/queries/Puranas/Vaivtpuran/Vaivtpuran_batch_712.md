# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 543.12554)
- **Original**: समस्त सिद्धोंके गुरु हैं; आपको नमस्कार है। थे। उनका नाम था--अष्टावक्र। वे ब्रह्मतेजसे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12555)
- **Original**: वेदोंक बीजस्वरूप परमात्मन्‌! आप वेदोंके ज्ञाता, प्रकाशित हो रहे थे। उनका मस्तक जटाओंसे भरा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12556)
- **Original**: बेदवान्‌ू और वेददेत्ताओंमें श्रेष्ठ हैं। बेद भी था और वे अपने मुँहसे आग उगल रहे थे, मानो
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12557)
- **Original**: आपको पूर्णतः नहीं जान सके हैं। रूपेश्वर! आप मुखद्वारसे उनकी तपस्याजनित तेजोराशि हो प्रकट
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12558)
- **Original**: वेदज्ञोंक भी स्वामी हैं; आपको नमस्कार है। आप हो रही हो। अथवा वे ऐसे लगते थे, मानो उनके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12559)
- **Original**: ब्रह्मा, अनन्त, शिव, शेष, इन्द्र और धर्म आदिके रूपमें स्वयं ब्रह्मतेज ही मूर्तिमान्‌-सा हो गया हो।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12560)
- **Original**: अधिपति हैं। सर्वस्वरूप सर्वेश्व! आप शर्व उनके नख और मूँछ-दाढ़ीके बाल बढ़े हुए थे।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12561)
- **Original**: (महादेवजी)-के भी स्वामी हैं; सबके बीजरूप वे तेजस्वी और परम शान्त थे तथा भयभीत हो
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12562)
- **Original**: गोविन्द! आपको नमस्कार है। आप ही प्रकृति भक्तिभावसे दोनों हाथ जोड़ मस्तक झुकाये हुए
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12563)
- **Original**: और प्राकृत पदार्थ हैं। प्राज्ञ, प्रकृतिके स्वामी तथा थे। उन्हें देख राधा हँसने लगीं; परंतु माधवने
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12564)
- **Original**: परात्पर हैं। संसार-वृक्ष तथा उसके बीज और उन्हें ऐसा करनेसे रोका और उन महात्मा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12565)
- **Original**: फलरूप हैं। आपको नमस्कार है। सृष्टि, पालन मुनौद्धके प्रभावका वर्णन किया। मुनिवर अष्टावक्रने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12566)
- **Original**: और संहारके बीजस्वरूप ब्रह्मा आदिके भी ईश्वर! गोविन्दको प्रणाम करके उनकी स्तुति कौ।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12567)
- **Original**: आप ही सृष्टि, पालन और संहारके कारण हैं। पूर्वकालमें महात्मा भगवान्‌ शंकरने उन्हें जिस
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12568)
- **Original**: महाविराट्‌ (नारायण)-रूपी वृक्षके बीज राधावह्लभ! हट 8 80 आपको नमस्कार है। अहो! आप जिसके बीज हैं, उस महाविराट्रूपी वृक्षके तीन स्कन्ध (तने) हैं--ब्रह्मा, विष्णु और शिव। वेदादि शास्त्र उसकी र शाखा-प्रशाखाएँ हैं और तपस्या पुष्प हैं। जिसका 'फल संसार है, वह वृक्ष प्रकृतिका कार्य है। आप 4]
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12569)
- **Original**: ही उसके भी आधार हैं, पर आपका आधार ह
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12570)
- **Original**: कोई नहीं है। सर्वाधार! आपको नमस्कार है। 9 तेज:स्वरूप ! निराकार! आपतक प्रत्यक्ष प्रमाणकी कै]
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12571)
- **Original**: पहुँच नहीं है। सर्वरूप! प्रत्यक्षक अविषय! हि 90“ # ल्‍£238
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12572)
- **Original**: स्वेच्छामय परमेश्वर! आपको नमस्कार है। स्तोत्नका उपदेश दिया था, उसीको उन्होंने सुनाया। यों कहकर मुनिश्रेष्ठ अष्टावक्र श्रीकृष्णके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12573)
- **Original**: » श्रीकृष्णजन्मसण्ड « 551 &6######%#4 45444 # 4 54 54444 % ऋ#ऋ#ऋऋ 484 8 % ऋ # ऋफ़ # 5 क $ 4 $ 5 कक ## # # 4 क # ## 8 ## 8 6 # 6 कक 89 «# चरणकमलॉोमें पड़ गये और श्रीराधा तथा गोविन्द
- **Translation**: 

---

