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

### Verse 1 (Bramha 0.1841)
- **Original**: अक्षय तृप्तिका सम्पादन करते हैं। दुराचारों तथा परद्रोही मनुष्य नहीं है। वहाँ सर्वत्र
- **Translation**: 

---

### Verse 2 (Bramha 0.1842)
- **Original**: स्रानके पश्चात्‌ मौन एवं जितेन्द्रिय भावसे सुखपूर्वक सब लोग घूमते-फिरते हैं। वह स्थान
- **Translation**: 

---

### Verse 3 (Bramha 0.1843)
- **Original**: भगवान्‌ शड्जभूरके मन्दिरमें प्रवेश करके उनकी सब जीवॉके लिये सुखद है। वहाँ नाना प्रकारके
- **Translation**: 

---

### Verse 4 (Bramha 0.1844)
- **Original**: पूजा करे। तीन बार शिवकी प्रदक्षिणा करे। घृत पक्षियॉंका कलर्व सुनायी पड़ता है। बहाँके, और दुग्ध आदिके द्वारा पत्रि्नतापूर्वक भगवान्‌ उद्यान नन्दनवनके समान एबं सबके सेवन करने , शझ्भुरको स्नान कराकर उनके सब अश्जोमें सुगन्धित योग्य हैं। वहाँके वृक्ष फलोंके भारसे झुके रहते हैं
- **Translation**: 

---

### Verse 5 (Bramha 0.1845)
- **Original**: चन्दन एवं केसर लगाये। तदनन्तर नाना प्रकारके और सभो ऋतुओंमें उनसे फूल झड़ते रहते हैं।
- **Translation**: 

---

### Verse 6 (Bramha 0.1846)
- **Original**: पवित्र पुष्पों तथा ब्रिल्वपत्र, आक और कमल दीर्षिका, तड़ाग, पुष्करिणी, वापी तथा अन्यान्य
- **Translation**: 

---

### Verse 7 (Bramha 0.1847)
- **Original**: आदिके द्वारा बैदिक एवं तान्त्रिक मन्त्रोंसे तथा जलाशय सदा कमलवनसे सुशोभित रहते हैं।। केवल नाममय मूल मन्त्रसे गन्ध, पुष्प, चन्दन,
- **Translation**: 

---

### Verse 8 (Bramha 0.1848)
- **Original**: * एकापग्रकक्षेत्र तथा पुरुषोत्तमक्षेत्रकी महिमा « धूप, दीप, नैवेद्य, उपहार, स्तुति, दण्डवत्‌-प्रणाम,
- **Translation**: 

---

### Verse 9 (Bramha 0.1849)
- **Original**: वहाँकी भूमिपर सब ओर बालू बिछी हुईं है। वह मनोहर गीत-वाद्य, नृत्य, जप, नमस्कार, जय-शब्द
- **Translation**: 

---

### Verse 10 (Bramha 0.1850)
- **Original**: परम पवित्र एवं सम्पूर्ण कामनाओंको देनेवाला तथा प्रदक्षिणा समर्पण करते हुए महादेवजीका
- **Translation**: 

---

### Verse 11 (Bramha 0.1851)
- **Original**: है। अशोक, अर्जुन, पुंनगाग, मौलसिरी, सरल, पूजन करे। इस प्रकार देवाधिदेवका विधिपूर्वक
- **Translation**: 

---

### Verse 12 (Bramha 0.1852)
- **Original**: कटहल, नारियल, शाखू, ताड़, कैथ, चम्पा, पूजन करनेवाला पुरुष सब पापोंसे मुक्त हो
- **Translation**: 

---

### Verse 13 (Bramha 0.1853)
- **Original**: कनेर, आम, बेल, गुलाब, कदम्ब, कचनार, शिवलोकमें जाता है। जो उत्तम बुद्धिवाले पुरुष
- **Translation**: 

---

### Verse 14 (Bramha 0.1854)
- **Original**: लकुच, नागकेसर, पीपल, छितबन, महुआ, सहिजन, वहाँ हर समय महादेवजीका दर्शन करते हैं, वे भी
- **Translation**: 

---

### Verse 15 (Bramha 0.1855)
- **Original**: शीशम, आँवला, नीम तथा बहेड़ा आदिके वृक्षोंसे पापमुकत होकर शिवलोकमें जाते हैं। भगवान्‌
- **Translation**: 

---

### Verse 16 (Bramha 0.1856)
- **Original**: उसकी बड़ी शोभा होती हैं। वहाँ पक्षियोंके शिवसे पश्चिम, पूर्व, दक्षिण, उत्तर-चारों ओर
- **Translation**: 

---

### Verse 17 (Bramha 0.1857)
- **Original**: मुखसे निकले हुए अत्यन्त मधुर कलरव कानों ढाई-ढाई योजनतक वह क्षेत्र भोग एवं मोक्ष प्रदान
- **Translation**: 

---

### Verse 18 (Bramha 0.1858)
- **Original**: और मनको बहुत सुख देते हैं। ऊपर बताये हुए करनेवाला है। उस उत्तम क्षेत्रमें भास्करेश्वर नामसे
- **Translation**: 

---

### Verse 19 (Bramha 0.1859)
- **Original**: वृक्षोके अतिरिक्त अन्यान्य मनोहर पुष्पों, लताओं प्रसिद्ध एक शियलिड्ग है। जो लोग वहाँ कुण्डमें
- **Translation**: 

---

### Verse 20 (Bramha 0.1860)
- **Original**: और भाँति-भाँतिके जलाशयोंसे वह क्षेत्र सुशोभित स्रान करके भगवान्‌ सूर्यद्वारा पूजित त्रिनेत्रधारी
- **Translation**: 

---

