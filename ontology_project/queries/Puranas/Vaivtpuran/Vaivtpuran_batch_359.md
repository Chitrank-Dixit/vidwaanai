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

### Verse 1 (Vaivtpuran 16.3674)
- **Original**: प्रतिज्ञा करता है, और फिर उस प्रतिज्ञाका पालन ऊपर तुलसीके पत्ते पड़े, इसी उद्देश्यसे वे सब
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3675)
- **Original**: नहीं करता, उसे सूर्य और चन्द्रमाकी अवधिपर्यन्त लोग वहाँ रहेंगे। तुलसीपत्रके जलसे जिसका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3676)
- **Original**: “कालसूत्र' नामक नरकमें यातना भोगनी पड़ती अभिषेक हो गया, उसे सम्पूर्ण तीर्थोंमें स्नान करने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3677)
- **Original**: है। जो मनुष्य तुलसीकों हाथमें लेकर या उसके तथा समस्त बज्ञोमें दीक्षित होनेका फल मिल
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3678)
- **Original**: निकट झूठी प्रतिज्ञा करता है, बह “कुम्भीपाक' गया। साध्वी! हजारों घड़े अमृतसे नहलानेपर भी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3679)
- **Original**: नामक नरकमें जाता है और वहाँ दीर्घकालतक भगवान्‌ श्रीहरिको उतनी तृप्ति नहीं होती है,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3680)
- **Original**: वास करता है। मृत्युके समय जिसके मुखमें जितनी वे मनुष्योंके तुलसीका एक पत्ता चढ़ानेसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3681)
- **Original**: तुलसीके जलका एक कण भी चला जाता है प्राप्त करते हैं। पतिब्रते! दस हजार गोदानसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3682)
- **Original**: वह अवश्य ही विष्णुलोकको जाता है। पूर्णिमा, मानव जो फल प्राप्त करता है, बही फल तुलसी-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3683)
- **Original**: अमाबास्या, ट्वादशी और सूर्य-संक्रान्तिक दिन, पत्रके दानसे पा लेता है। जो मृत्युके समय मुखमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3684)
- **Original**: मध्याहकाल, रात्रि, दोनों संध्याओं और अशौचके तुलसी-पत्रका जल पा जाता है, वह सम्पूर्ण (समय, तेल लगाकर, बिना नहाये-धोये अथवा पापोंसे मुक्त होकर भगवान्‌ विष्णुके लोकमें चला
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3685)
- **Original**: ग़तके कपड़े पहने हुए जो मनुष्य तुलसीके जाता है। जो मनुष्य नित्यप्रति भक्तिपूर्वक तुलसीका
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3686)
- **Original**: पत्रोंको तोड़ते हैं, वे मानो भगवान्‌ श्रीहरिका जल ग्रहण करता है, वही जीवन्मुक्त है और उसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3687)
- **Original**: मस्तक छेदन करते हैं। साध्यि
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3688)
- **Original**: श्राद्ध, व्रत, दान, गड्जा-स्नानका फल मिलता है। जो मानव प्रतिदिन
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3689)
- **Original**: प्रतिष्ठा तथा देवार्चनके लिये तुलसीपत्र बासी तुलसीका पत्ता चढ़ाकर मेरी पूजा करता है, वह
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3690)
- **Original**: होनेपर भी तीन राततक पवित्र हो रहता है। लाख अश्वमेध-यज्ञोंका फल पा लेता है। जो पृथ्वीपर अथवा जलमें गिरा हुआ तथा श्रीविष्णुकों मानव तुलसीको अपने हाथमें लेकर और शरीरपर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3691)
- **Original**: अर्पित तुलसी-पत्र धो देनेपर दूसरे कार्यके लिये रखकर तीथथोंमें प्राण त्यागता है, वह विष्णुलोकमें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3692)
- **Original**: शुद्ध माना जाता है।* *तव केशसमूहाक्ष पुण्यवृक्षा. भवन्त्विति । तुलसीकेशसम्भूतास्तुलसीति च। बिश्वुता:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3693)
- **Original**: त्रिपु लोकेषु. पुष्पाणां पत्राणां देवपूजने । प्रधानरूपा तुलसी अभविष्यति बरानने
- **Translation**: 

---

