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

### Verse 1 (Vaivtpuran 4.8807)
- **Original**: घिरा हुआ है। वे गोपकुमारियाँ रत्नोंके बने हुए देवेश्वर नदीके उस पार गये। वहाँ जानेपर उन्हें [कंगन, बाजूबंद और नूपुरोंसे विभूषित हैं। पर्वतोंमें श्रेष्ठ शतभ्ृृंग दिखायी दिया, जो अपनी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8808)
- **Original**: रत्रनिर्मित युगल कुण्डल उनके गण्डस्थलकी शोभासे मनको मोहे लेता था। दिव्य पारिजात-
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8809)
- **Original**: शोभा बढ़ाते हैं। उनके हाथोंकी अंगुलियाँ रत्रोंकी वृक्षोंकी वनमालाएँ उसकी शोभा बढ़ा रही थीं।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8810)
- **Original**: बनी हुई अँगूठियोंसे विभूषित हो बड़ी सुन्दर वह पर्वत कल्पवृक्षों तथा कामधेनुओंद्वारा सब
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8811)
- **Original**: दिखायी देती हैं। रत्रमय पाशकसमूहों (बिछुओं)- ओरसे घिरा था। उसकी ऊँचाई एक करोड़ योजन
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8812)
- **Original**: से उनके पैरोंकी अंगुलियाँ उद्धासित होती हैं। थी और लंबाई दस करोड़ योजन
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8813)
- **Original**: उसके ऊपरकी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8814)
- **Original**: वे गोपकिशोरियाँ रत्रमय आभूषणोंसे विभूषित हैं। चौरस भूमि पचास करोड़ योजन विस्तृत थी।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8815)
- **Original**: उनके मस्तक उत्तम रज्नमय मुकुटोंसे जगमगा रहे वह पर्वत चहारदीवारीकी भाँति गोलोकके चारों
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8816)
- **Original**: हैं। नासिकाके मध्यभागमें गजमुक्ताकी बुलाकें ओर फैला हुआ था। उसीके शिखरपर उत्तम
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8817)
- **Original**: बड़ी शोभा दे रही हैं। उनके भालदेशमें सिन्दूरकी गोलाकार रासमण्डल है, जिसका विस्तार दस
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8818)
- **Original**: बेंदी लगी हुई है। साथ ही आभूषण पहननेके योजन है। वह रासमण्डल सुगन्धित पुष्पोंसे भरे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8819)
- **Original**: स्थानोंमें दिव्य आभूषण धारण करनेके कारण हुए सहस्रों उद्यानोंसे सुशोभित है और उन
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8820)
- **Original**: उनकी दिव्य प्रभा और भी उद्दी्त हो उठी है। उद्यानोंमें भ्रमर-समूह छाये रहते हैं। सुन्दर रत्नों
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8821)
- **Original**: उनकी अज्जकान्ति मनोहर चम्पाके समान जान और द्रव्योंसे सम्पन्न अगणित क्रीडाभवन तथा पड़ती है। वे सब-की-सब चन्दन-द्रवसे चर्चित कोटि सहस्र रत्रमण्डप उसकी शोभा बढ़ाते हैं।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8822)
- **Original**: हैं। उनके अड्रोंपर पीले रंगकी रेशमी साड़ी शोभा रत्रमयी सीढ़ियों, श्रेष्ठ रत्ननिर्तित कलशों तथा देती है। बिम्बफलके समान अरुण अधर उनकी इन्द्रनीलमणिके शोभाशाली खम्भोंसे उस मण्डलकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8823)
- **Original**: मनोहरता बढ़ा रहे हैं। शरत्कालकी पूर्णिमाके शोभा और बढ़ गयी है। उन खम्भोंमें सिन्दूरके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8824)
- **Original**: चन्द्रमाओंकी चटकीली चौंदनी-जैसी प्रभासे सेवित समान रंगवाली मणियाँ सब ओर जड़ी गयी हैं [मुख उनके उद्दीत सौन्दर्यकों और भी उज्ज्वल तथा बीच-बीचमें लगे हुए मनोहर इन्द्रनील
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8825)
- **Original**: बना रहे हैं। उनके नेत्र शरत्कालके प्रफुल्ल नामक रत्नोंसे वे मण्डित हैं। रत्रमय परकोटोंमें
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8826)
- **Original**: कमलॉकी शोभाको छीने लेते हैं। उनमें कस्तूरी- जटित भाँति-भाँतिके मणिरत्ञ उस रासमण्डलकी
- **Translation**: 

---

