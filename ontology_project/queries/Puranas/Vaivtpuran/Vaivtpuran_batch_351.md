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

### Verse 1 (Vaivtpuran 16.3514)
- **Original**: पश्चात्‌ कार्तिकेय फिर सचेत हो गये। उन्होंने वह लगी। स्कन्दका युद्ध अत्यन्त अद्भुत और भयानक
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3515)
- **Original**: दिव्य धनुष हाथमें लिया, जिसे पूर्वकालमें था। वह प्राकृतिक प्रलयकी भाँति दानवोंके लिये
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3516)
- **Original**: भगवान्‌ विष्णुने प्रदान किया था। फिर रह्रेन्द्रसारसे विनाशकारी सिद्ध हो रहा था। उसे देखकर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3517)
- **Original**: निर्मित यानपर आरूढ़ हो अस्त्र-शस्त्र लेकर विमानपर बैठे हुए राजा शह्बुचूड़ने बाणोंकी वर्षा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3518)
- **Original**: कार्तिकय भयंकर युद्ध करने लगे। शिवकुमार आरम्भ कर दी। राजाके बाण इस तरह गिर रहे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3519)
- **Original**: स्कन्दने अपने दिव्यास्त्रसे क्रोधपूर्वक दानवराजके थे, मानो मेघ जलकी धारा गिरा रहा हो। वहाँ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3520)
- **Original**: चलाये हुए समस्त पर्वतों, शिलाखण्डों, सर्पों और घोर अन्धकार छा गया। फिर आग प्रकट होने
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3521)
- **Original**: वृक्षोंको काट गिराया। उन प्रतापी बीरने पार्ज॑न्यास्त्रके लगी। यह देख नन्‍्दीश्वर आदि सब देवता वहाँसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3522)
- **Original**: द्वारा आग बुझा दी और खेल-खेलमें ही शह्भुचूड़के भाग चले। केवल कार्तिकेय ही युद्धके मुहानेपर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3523)
- **Original**: रथ, धनुष, कवच, सारथि और उण्ज्वल किरीट- डटे रहे। राजा शद्भुचूड़ पर्वतों, सर्पों, शिलाओं
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3524)
- **Original**: मुकुटकों काट डाला। फिर उल्काके समान तथा वृक्षोंकी भयानक वृष्टि करने लगा। उसका
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3525)
- **Original**: प्रकाशित होनेवाली अपनी शक्ति दानवराजके वेग दुःसह था। राजाकी बाणवर्षासे शिवकुमार
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3526)
- **Original**: वक्षःस्थलपर दे मारी। उसके आघातसे राजा कार्तिकेव ढक गये, मानो सूर्यदेबपर ल्िग्ध
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3527)
- **Original**: मूच्छित हो गया। फिर तुरंत ही होशमें आकर वह मेघमालाका आवरण पड़ गया हो। शड्डचूड़ने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3528)
- **Original**: दूसरे रथपर जा चढ़ा और दूसरा धनुष हाथमें ले
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3529)
- **Original**: #प्रकृत्तिसण्ड + 159 6468###%#& 66868 84 4 #& 8 ## # 848 68 6844 # 86688 68 6868 ## 86 # 5 ###8##8#%# 4 # 5 8 8 5 8 5 4 / 85 ऋ हक 4 क इक लिया। नारद! शह्लुचूड़ मायावियोंका शिरोमणि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3530)
- **Original**: विश्व और पलाश--इन सबके साथ आदित्यगण था। उसने मायासे उस युद्धभूमिमें बाणोंका जाल
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3531)
- **Original**: घोर युद्ध करने लगे। ग्यारह महारुद्रगण ग्यारह बिछा दिया और उसके द्वारा कार्तिकयकों ढककर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3532)
- **Original**: भयंकर दानवोंके साथ भिड़ गये। उग्रदण्डा आदि सैकड़ों सूर्योके समान प्रकाशित होनेवाली एक
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3533)
- **Original**: और महामारीमें युद्ध होने लगा। नन्दीश्वर आदि अमोघ शक्ति हाथमें ली। भगवान्‌ विष्णुके तेजसे
- **Translation**: 

---

