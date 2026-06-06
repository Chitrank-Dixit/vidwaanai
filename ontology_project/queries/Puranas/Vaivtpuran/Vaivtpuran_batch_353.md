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

### Verse 1 (Vaivtpuran 16.3554)
- **Original**: विक्षत हुए महान्‌ बल-पराक्रमसे सम्पन्न सभी चघृतपृष्ठमें तथा रक्ताक्ष और शबनैश्नरमें युद्ध होने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3555)
- **Original**: दानव भयके मारे भाग चले। वृषपर्वा, विप्रचित्ति, लगा। जयन्तने रत्नसारका सामना किया। वसुगण
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3556)
- **Original**: दम्भ और विकड्भून--ये सब बारी-बारीसे स्कन्दके और वर्चोगण परस्पर जूझने लगे। दीप्तिमान्‌के
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3557)
- **Original**: साथ युद्ध करने लगे। अब कालीने समराद्भणमें साथ अश्विनीकुमार और धूम्रके साथ नलकूबरका
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3558)
- **Original**: प्रवेश किया। भगवान्‌ शिव कार्तिकेयकी रक्षा युद्ध आरम्भ हुआ। धर्म और धनुर्धर, मड्रल और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3559)
- **Original**: करने लगे। नन्दीश्वर आदि वीर कालीके ही मण्डूकाक्ष, शोभाकर और ईशान तथा पीठर और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3560)
- **Original**: पीछे-पीछे गये। समस्त देवता, गन्धर्व, यक्ष, मनन्‍्मथ एक-दूसरेका सामना करने लगे। उल्कामुख,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3561)
- **Original**: राक्षस, किन्नर, बहुत-से राज्यभाण्ड और करोड़ों धूप्र, खड्गध्वज, काझ्लीमुख, पिण्ड, धूम्र, नदी,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3562)
- **Original**: मेघ भी उन्होंके साथ थे। संग्राममें पहुँचकर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3563)
- **Original**: कालीने सिंहनाद किया। देवीके उस सिंहनादसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3564)
- **Original**: पाशुपत-अस्त्रको हाथमें उठा लिया और उसे दानव मूच्छित हो गये। कालीने बारंबार दैत्योंक
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3565)
- **Original**: चलाना ही चाहती थीं कि उन्हें मना करती हुई लिये अमज्जलसूचक अट्टहास किया। वे युद्धके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3566)
- **Original**: यह स्पष्ट आकाशवाणी हुई--'यह राजा एक मुहानेपर हर्षपूर्वक मधु पीने और नृत्य करने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3567)
- **Original**: महान्‌ पुरुष है, इसकी मृत्यु पाशुपत-अस्त्रसे लगीं। उग्रदंष्टा, उग्रचण्डा और कौट्टरी भी मधु-
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3568)
- **Original**: कदापि नहीं होगी। जबतक यह अपने गलेमें पान करने लगीौं। योगिनियों और डाकिनियोंके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3569)
- **Original**: भगवान्‌ श्रीहरिंके मन्त्रका कवच धारण किये गण तथा देवगण आदि भी इस कार्यमें योग देने
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3570)
- **Original**: रहेगा और जबतक इसकी पतिब्रता पत्नी अपने लगे। कालीको उपस्थित देख शब्बुचूड़ तुरंत
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3571)
- **Original**: सतीत्वकी रक्षा करती रहेगी, तबतक इसके रणभूमिमें आ पहुँचा। दानव डरे हुए थे।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3572)
- **Original**: समीप जरा और मृत्यु अपना कुछ भी प्रभाव नहीं दानवराजने उन सबको अभय दान दिया। कालोने
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3573)
- **Original**: डाल सकती-यह त्रह्माका वर है।' प्रलयाग्रिकी शिखाके समान अग्नि फेंकना आरम्भ
- **Translation**: 

---

