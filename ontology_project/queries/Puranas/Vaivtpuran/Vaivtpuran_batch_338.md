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

### Verse 1 (Vaivtpuran 16.3254)
- **Original**: नक्षत्रोंक बीच चन्द्रमा हो। देवताओंसहित ब्रह्मा सभामें पहुँचे। उस सभाभवनमें चारों ओर देवर्षि
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3255)
- **Original**: और शंकरने उनके साक्षात्‌ दर्शन किये। उस तथा पार्षद विराजमान थे। सभी पार्षदोंके चार
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3256)
- **Original**: समय श्रीहरि दिव्य रज्नोंसे निर्मित अद्भुत सिंहासनपर भुजाएँ थीं; सबका रूप भगवान्‌ नारायणके समान
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3257)
- **Original**: विराजित थे। दिव्य किरीट, कुण्डल और था और सभी कौस्तुभमणिसे अलंकृत थे। बह
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3258)
- **Original**: बनमालाने उनकी छबिको और भी अधिक बढ़ा सभा बाहरसे पूर्ण चन्द्रमण्डलके आकारकी गोल
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3259)
- **Original**: दिया था। उनके सम्पूर्ण अड्भ चन्दनसे अनुलिप्त और भीतरसे चौकोर थी। बड़ी मनोहर दिखायी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3260)
- **Original**: थे। एक हाथमें कमल शोभा पा रहा था। देती थी। श्रेष्ठ रत्नोंके सारभूत सर्वोत्तम दिव्य
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3261)
- **Original**: भगवान्‌का श्रीविग्रह अतिशय शान्त था। लक्ष्मीजी मणियोंसे उसका निर्माण हुआ था। होरोंके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3262)
- **Original**: उनके चरणकमलोंकी सेवामें संलग्न थीं। भक्तके सारभागसे ही वह सजी हुई थी। श्रीहरिके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3263)
- **Original**: दिये हुए सुवासित ताम्बूलको प्रभु चबा रहे थे। इच्छानुसार बने हुए उस भवनमें अमूल्य दिव्य
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3264)
- **Original**: देवी गज्जा उत्तम भक्तिक साथ सफेद चँँबर रत्न जड़े गये थे। माणिक्य-मालाएँ जालीके रूपमें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3265)
- **Original**: डुलाकर उनकी सेवा कर रहीं थीं। उपस्थित शोभा दे रही थीं और दिव्य मोतियोंकी झालरें [समाज अत्यन्त भक्तिविनग्र होकर उनका स्तव- उसकी छबि बढ़ा रही थीं। मण्डलाकार करोड़ों
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3266)
- **Original**: गान कर रहा था।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3267)
- **Original**: मुने! ऐसे परम विशिष्ट परिपूर्णतम भगवान्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3268)
- **Original**: ही शापका पालन करके पुनः: लौट आयेगा। श्रीहरिके दर्शन प्राप्त होनेपर ब्रह्मा प्रभूति समस्त
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3269)
- **Original**: 'सुदामन्‌! तुम यहाँ अवश्य आ जाना'-यों भगवद्धक्त देवता भयभीत-से होकर भक्तिभावसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3270)
- **Original**: कहकर मैंने किसी प्रकार राधाकों शान्त किया। गर्दन झुकाये उन्हें प्रणाम करके स्तुति करने लगे।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3271)
- **Original**: अखिल जगतके रक्षक ब्रह्मन्‌ंं गोलोकके आधे उस समय हर्षके कारण उनके सर्बाज्रमें पुलकावली
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3272)
- **Original**: क्षणमें ही भूमण्डलपर एक मन्वन्तरका समय हो छा गयी थी, आँखोंमें आँसू भर आये थे और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3273)
- **Original**: जाता है। वाणी गद़द थी। परम श्रद्धाके साथ उपासना ब्रह्मन्‌! इस प्रकार यह सब कुछ पूर्वनिश्चित करके जगतके व्यवस्थापक ब्रह्माजीने हाथ
- **Translation**: 

---

