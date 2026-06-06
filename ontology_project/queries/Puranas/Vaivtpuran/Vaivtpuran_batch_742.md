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

### Verse 1 (Vaivtpuran 543.13154)
- **Original**: आये। वहाँ उन्हें आँगनमें खड़ा हुआ एक भिश्चु ही मधुर था। वह मनोहर नृत्य करते हुए मेरे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13155)
- **Original**: दिखायी दिया, जो बड़ा मनोहर था। उसके गुणोंका गान करने लगा। कभी श्रृद्र बजाता
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13156)
- **Original**: विषयमें मेनाके मुखसे सब बातें सुनकर हिमवान्‌ और कभी डमरू। उसके बाजेकी आवाज हँसे और रुष्ट भी हुए। उन्होंने अपने सेवककों सुनकर बहुत-से नागरिक हर्षविद्ल हो वहाँ आ
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13157)
- **Original**: आज्ञा दी--'इस भिक्षुकको बाहर निकाल गये। दर्शकोंमें बालक, बालिका, वृद्ध, युवक,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13158)
- **Original**: दो।' परंतु बह कोई साधारण भिक्षुक नहीं था। युवतियाँ तथा वृद्धाएँ भी थीं। मधुर तान और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13159)
- **Original**: आकाशकी भाँति उसका स्पर्श करना भी कठिन स्वस्से युक्त उस सुन्दर गीतकों सुनकर सहसा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13160)
- **Original**: था। वह अपने तेजसे प्रज्वलित हो रहा था। सब लोग मोहित एवं मूर्च्छित हो गये। दुर्गाकों
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13161)
- **Original**: उसे कोई बाहर न कर सका। उसके निकट भी मूर्छछा आ गयी। उसने अपने हृदयमें भगवान्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13162)
- **Original**: जानेकी भी किसीमें क्षमता नहीं थी। हिमवानने शंकरको देखा। वे त्रिशूल, पट्टिश और व्याप्रचर्म
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13163)
- **Original**: एक ही क्षणमें देखा--उस भिश्ुकके सुन्दर चार धारण किये सम्पूर्ण अड्रॉमें विभूतिसे विभूषित
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13164)
- **Original**: भुजाएँ हैं; मस्तकपर किरीट, कानोंमें कुण्डल थे। बड़ा ही रम्य रूप था। गलेमें अत्यन्त निर्मल [तथा शरीरपर पीताम्बर शोभा पाता हैं; श्याम- अस्थियोंकी माला शोभा देती थी। प्रसन्नमुखपर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13165)
- **Original**: सुन्दर रुचिर बेष मनको मोहे लेता है; मुखपर मनन्‍्द हास्यथकी छटा छा रही थी। उनकी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13166)
- **Original**: मन्द मुस्कानकी प्रभा फैल रही है। सम्पूर्ण अड्ड आकृतिसे आन्तरिक उल्लास सूचित होता था।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13167)
- **Original**: चन्दनसे चर्चित हैं तथा वे श्रीहरि (रूपधारी पाँच मुख और प्रत्येक मुखमें तीन-तीन नेत्र
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13168)
- **Original**: शिव) भक्तोंपर अनुग्रह करनेके लिये कातर शोभा पाते थे। हाथमें माला, कंधेपर नागोंका
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13169)
- **Original**: जान पड़ते हैं। यज्ञोपवीत और मस्तकपर चन्द्राकार मुकुट--बड़ी हिमवान्‌ श्रीहरिके उपासक थे। उन्होंने सुन्दर झाँकी थी। वे पार्वतीसे कह रहे थे कि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13170)
- **Original**: पूजाकालमें भगवान्‌ गदाधरको जो-जो फूल वर माँगो। हृदयस्थित हरको देखकर पार्वतीने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13171)
- **Original**: चढ़ाये थे, वे सब भिक्षुकके अड्भमें और
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13172)
- **Original**: मस्तकपर देखे। उनके द्वारा जो धूप-दीप दिये
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13173)
- **Original**: ही क्षणमें तेज:स्वरूप, निराकार, निरञ्जन, निर्लिस, गये थे, अथवा जो मनोरम नैवेद्य निवेदित हुआ
- **Translation**: 

---

