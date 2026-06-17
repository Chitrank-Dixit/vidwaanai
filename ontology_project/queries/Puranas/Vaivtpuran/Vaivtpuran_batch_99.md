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

### Verse 1 (Vaivtpuran 7.9713)
- **Original**: उत्सवके बिना भी यदि केवल उपवासमात्र कर ऐसा ही कहा था। जो अष्टमीको उपवास एवं
- **Translation**: 

---

### Verse 2 (Vaivtpuran 7.9714)
- **Original**: लें तो भगवान्‌ माधव उनपर उतनेसे ही प्रसन्न जागरणपूर्वक व्रत करता है, वह करोड़ों जम्मोंमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 7.9715)
- **Original**: हो जाते हैं। भक्तिभावसे भाँति-भाँतिके उपचार
- **Translation**: 

---

### Verse 4 (Vaivtpuran 7.9716)
- **Original**: 438 संक्षिप्त ब्रह्मवैवर्तपुराण « ####%%#%#########%##ऋ#ऋऋऋऋ 5 # 4 #########ऋकऋऊऋकऋऋककककअऋकऊऋऊऋऊऋडऋऊऋडकिफकऋऋऋऋ कक क चढ़ाने तथा रातमें जागरण करनेसे दैत्यशत्रु श्रीहरि
- **Translation**: 

---

### Verse 5 (Vaivtpuran 7.9717)
- **Original**: तिथिको जागरणपूर्वक ब्रतका अनुष्ठान करके जयन्ती-ब्रतका फल प्रदान करते हैं। जो अष्टमी-
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.9718)
- **Original**: मनुष्य सौ जन्मोंके किये हुए पापोंसे छुटकारा ब्रतके उत्सवमें धनका उपयोग करनेमें कंजूसी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.9719)
- **Original**: पा जाता है। इसमें संशय नहीं है। जो मनुष्य नहीं करता, उसे उत्तम फलकी प्राप्ति होती है।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.9720)
- **Original**: शुद्धा जन्माष्टमीमें केबल उपवासमात्र करके रह जो कंजूसी करता है, वह उसके अनुरूप ही
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.9721)
- **Original**: जाता है, ब्रतोत्सव या जागरण नहीं करता, वह फल पाता है। विद्वान्‌ पुरुष अष्टमी और रोहिणीमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.9722)
- **Original**: अश्वमेध-यज्ञके. फलका भागी होता है। पारणा न करे; अन्यथा वह पारणा पूर्वकृत
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.9723)
- **Original**: श्रीकृष्णजन्माष्टमीके दिन भोजन करनेवाले नराधम पुण्योंको तथा उपबाससे प्राप्त होनेवाले फलकों
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.9724)
- **Original**: घोर पापों और उनके भयानक फलोंके भागी भी नष्ट कर देती है, तिथि आठ गुने फलका
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.9725)
- **Original**: होते हैं। जो उपवास करनेमें असमर्थ हो, वह नाश करती है और नक्षत्र चौगुने फलका। अत:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.9726)
- **Original**: एक ब्राह्मणको भोजन कराबे अथवा उतना धन प्रयन्नपूर्वकतक तिथि और नक्षत्रके अन्तमें पारणा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.9727)
- **Original**: दे दे, जितनेसे वह दो बार भोजन कर ले। अथवा करे। यदि महानिशा प्राप्त होनेपर तिथि और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.9728)
- **Original**: प्राणायाम-मन्त्रपूर्वक्क एक सहस््र गायत्रीका जप नक्षत्रका अन्त होता हो तो ब्रती पुरुषको तीसरे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.9729)
- **Original**: करे। मनुष्य उस ब्रतमें बारह हजार मन्त्रोंका दिन पारणा करनी चाहिये। आदि और अन्तके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.9730)
- **Original**: यथार्थरूपसे जप करे तो और उत्तम है। वत्स चार-चार दण्डको छोड़कर बीचकी तीन पहरवाली
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.9731)
- **Original**: नारद! मैंने धर्मदेवके मुखसे जो कुछ सुना था, रात्रिको त्रियामा रजनी कहते हैं। उस रजनीके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 7.9732)
- **Original**: वह सब तुम्हें कह सुनाया। व्रत, उपवास और आदि और अन्तमें दो संध्याएँ होती हैं। जिनमेंसे पूजाका जो कुछ विधान है और उसके न एकको दिनादि या प्रातःसंध्या कहते हैं और
- **Translation**: 

---

