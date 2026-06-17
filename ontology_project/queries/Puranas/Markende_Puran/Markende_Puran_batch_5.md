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

### Verse 1 (Markende Puran 0.81)
- **Original**: जैमिनि, विन्ध्यपर्वंतपर, जहाँ ये धर्मात्मा पक्षी निवास करते हैं। तुम उन्तकी सेवामें जाओ और
- **Translation**: 

---

### Verse 2 (Markende Puran 0.82)
- **Original**: रहते थे, गये। उस पर्वतके निकट पहुँचनेपर पाठ उनसे झ्वातव्य बातें पूछों। करते हुए उन पक्षिग्रोंकों ध्वनि उनके कानोंमें * शगातू काम; प्रशबति कापाल्‍लोभो$भिलावते। लोभाद्धयति सम्मोह: सम्मोहात्‌ स्टृतित्रिग्रस:
- **Translation**: 

---

### Verse 3 (Markende Puran 0.83)
- **Original**: स्मृशिभ्रशाद बुद्धिनाशों भुद्धिनाशात्‌ ?णश्याति
- **Translation**: 

---

### Verse 4 (Markende Puran 0.84)
- **Original**: (3। 71-72 ) पृतास्थसाविक संसरे थो न दविशैन वाध्यते! रूर्ेणमेठ उन्तृरं ईछाथोत्ं हि चैटितेम! (3
- **Translation**: 

---

### Verse 5 (Markende Puran 0.85)
- **Original**: 10 + संक्षिम मार्कणकेय पुराण * म-+ह3ल्‍548+“किड- ऐसा &- रहते हैं। बन अपने मनमें और इस प्रकार सोचने लगे--' अहो। ये श्रेष्ठ पक्षो दाद, कपल कह “7 4म4348_27-कृट)अ.->+र-बा 8 6 #> चाहिये। शोक्त और हर्षके त्रशीधृत्त न होना हैं; जिस अक्षरका कण्ट- तालु आदि जो स्थान है, करता चार हक उसका भहींसे उच्चाएण हो रहा है। बोलनेमें
- **Translation**: 

---

### Verse 6 (Markende Puran 0.86)
- **Original**: ही ज्ञानका 5144, “64 की 27-30 की- केक आअआ1+ 9-7
- **Translation**: 

---

### Verse 7 (Markende Puran 0.87)
- **Original**: अर्घ्यके द्वारा महर्षि जैमिनिका पूजन किया और करते जा रहे हैं, रुककर साँसतक नहीं लेते) (समन मकर अप "कोड पल 3-क-)330%43%#07-+ैन की अपने पंखोंसे हवा करके उनकी धब्ह्ावर दूर की। 3 2-3 ऑ-सेल्‍रपकल +म जब बे सुखपूर्वक बैठकर विश्नाम ले चुके, तब दिखायी देता। ये व्पि निन्दित योनिक्ो प्राप्त **
- **Translation**: 

---

### Verse 8 (Markende Puran 0.88)
- **Original**: पलक 21085 जकट अर्यंकी हे है
- **Translation**: 

---

### Verse 9 (Markende Puran 0.89)
- **Original**: हो गया। यह जीवन भो ठत्तम जीवत बन गया; यह मुझे बड़े आश्चर्यकी बात जान पड़ती है।
- **Translation**: 

---

### Verse 10 (Markende Puran 0.90)
- **Original**: वर पा मे लक समर भक 5.2 33%+5 18037060-#0अ->ि
- **Translation**: 

---

### Verse 11 (Markende Puran 0.91)
- **Original**: दशन मिला, जो देवताओंके लिये भी बन्दनीय हज 20 1:30 03 1-4] हैं। हमारे शरीरमें पिलाजोके क्रोधसे प्रकट हुई जो 5 मसाज पाप कह अमनिंग
- **Translation**: 

---

### Verse 12 (Markende Puran 0.92)
- **Original**: औिण जल रही" वह आज आपके दर्शनरूपी जा पा शतक जलसे सिंचकर शान्त हो गयो। अह्मम! आप अपनाया पर धि साकरापा बह इक
- **Translation**: 

---

### Verse 13 (Markende Puran 0.93)
- **Original**: कुशलसे तो हैं न? आपके आम्रपमें रहनेवाले 8341-94 30000: । मृंग, पश्नी, सक्ष, लता, गुल्मं, बॉस और भाँति- िलनरे> हक क नह जी तेके (ण- सबको शल है न? इनपर कै आवक पिन काका बेवा जे
- **Translation**: 

---

### Verse 14 (Markende Puran 0.94)
- **Original**: +3-व नह ह है 6.24 कृषा कीजिये $2- -शमिनल- सेल और यहाँ अपने आगमनका कारण बतलाहये। दीप" 25054 अं हैक
- **Translation**: 

---

### Verse 15 (Markende Puran 0.95)
- **Original**: हमारा कोई बहुत बड़ा भाग्य था, जो आप इत कक चल ओधी
- **Translation**: 

---

### Verse 16 (Markende Puran 0.96)
- **Original**: का भोले कह पक्षीगण! मुझे घहाभारत- आपको पक्षियोंकी योनिमें आना (40 उसके 70-00 पी - की वका8020.289 14 लिये खेद नहीं करना चाहिये; क्योंकि वह स्वंधा
- **Translation**: 

---

### Verse 17 (Markende Puran 0.97)
- **Original**: / 12 ीकृककी- +लऔ57 दैठका हो विधान था। तपस्याका क्षय हो जानेपर पहले भव 40+-
- **Translation**: 

---

### Verse 18 (Markende Puran 0.98)
- **Original**: 0:+2- महहर थो पके इक करे 4 22 4
- **Translation**: 

---

### Verse 19 (Markende Puran 0.99)
- **Original**: मदिकवपकापर द्रोणके पृत्र महात्मा पक्ठी रहते हैं। कल" रहे कक का अब कि लअ
- **Translation**: 

---

### Verse 20 (Markende Puran 0.100)
- **Original**: ने तुम्हारे प्रश्नोंका विस्तारपूर्बक्त उत्तर देंगे।' पहले गो गिराक्र द्ठ सा कप सह शक ये जाते हैं। इस प्रकार आनेबालीं विपरीत । उनकी विकार कप सासलो पक दर्शाएँ मैंने अनेक थार देखी हैं। भावक बाद हूँ। 2264038
- **Translation**: 

---

