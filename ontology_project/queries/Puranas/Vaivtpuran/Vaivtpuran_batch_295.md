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

### Verse 1 (Vaivtpuran 13.12042)
- **Original**: एकादशीको ही उपवास-ब्रत करते हैं। अतः ब्रतका पालन अवश्य करना चाहिये। सचमुच ही
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12043)
- **Original**: नारद! उनके लिये कृष्णा एकादशीका लक्बून ब्रह्महत्या आदि सारे पाप एकादशौके दिन चावल
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12044)
- **Original**: करनेपर भी वेदोंमें दोष नहीं बताया गया है। (भात)-का आश्रय लेकर रहते हैं। जो मन्द-
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12045)
- **Original**: हरिशयनी और हरिबोधिनी--इन दो एकादशियोंके बुद्धि मानव इतने पापोंका भक्षण करते हुए चावल
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12046)
- **Original**: बीचमें जो कृष्णा एकादशियाँ आती हैं, उन्होंमें खाता है, वह इस लोकमें अत्यन्त पातकी है और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12047)
- **Original**: गृहस्थ पुरुषकों उपवास करना चाहिये। इनके अन्तमें निश्चय ही नरकगामी होता है। दशमीके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12048)
- **Original**: सिवा दूसरी किसी कृष्णपक्षकी एकादशीमें गृहस्थ लक्बुनमें जो दोष है, उसे बताता हूँ; सुनो।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12049)
- **Original**: पुरुषको उपवास नहीं करना चाहिये। ब्रह्मन्‌! इस पूर्वकालमें धर्मके मुखसे मैंने इसका श्रवण किया
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12050)
- **Original**: प्रकार एकादशीके विषयमें निर्णय कहा गया, जो था। जो मूढ़ जान-बूझकर कलामात्र दशमीका
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12051)
- **Original**: श्रुतिमें प्रसिद्ध है। अब इस ब्रतका विधान बताता लड्डन करता है, उसे तुरंत ही दारुण शाप देकर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12052)
- **Original**: हूँ, सुनो। लक्ष्मी उसके घरसे निकल जाती हैं। इस लोकमें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12053)
- **Original**: . दशमीके दिन पूर्वाह्ममें एक बार हविष्यान्न निश्चय ही उसके वंशकी और यशकौ भी हानि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12054)
- **Original**: भोजन करे। उसके बाद उस दिन फिर जल होती है। जिस दिन दशमी, एकादशी और द्वादशी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12055)
- **Original**: भी न ले। रातमें कुशकी चटाईपर अकेला शयन तीनों तिथियाँ हों, उस दिन भोजन करके दूसरे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12056)
- **Original**: करे और एकादशीके दिन ब्राह्ममुहूर्तमें उठकर दिन उपवास-ब्रत करना चाहिये। द्वादशीको ब्रत
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12057)
- **Original**: प्रातःकालिक कार्य करके नित्य-कृत्य पूर्ण करके त्रयोदशीको पारण करना चाहिये। उस
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12058)
- **Original**: करनेके पश्चात्‌ स्नान करें। फिर श्रीकृष्णकी दशामें व्रतधारियोंकों द्वादशी-लद्भनसे दोष नहीं
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.12059)
- **Original**: प्रसन्नताके उद्देश्यसे ब्रतोपवासका संकल्प लेकर होता। जब पूरे दिन और रातमें एकादशी हो तथा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12060)
- **Original**: संध्या-तर्पण करनेके अनन्तर नैत्यिक पूजन आदि उसका कुछ भाग दूसरे दिन प्रातःकालतक ल्‍ करे। दिनमें मैत्यिक पूजन करके व्रतसम्बन्धी गया हो, तब दूसरे दिन ही उपवास करना
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12061)
- **Original**: आवश्यक सामग्रीका संग्रह करे। षोडशोपचार- चाहिये। यदि परा तिथि बढ़कर साठ दण्डकी हो
- **Translation**: 

---

