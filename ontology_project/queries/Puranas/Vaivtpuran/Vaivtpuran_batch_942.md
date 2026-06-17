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

### Verse 1 (Vaivtpuran 543.17154)
- **Original**: करके शुद्ध हो धुली हुई साड़ी और कंचुकी धारण बलशाली नरेशों और असुरों, अन्यान्य महाबली
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17155)
- **Original**: की। फिर भुवनपावनी कान्ता राधाने अपने गन्धर्वों तथा राक्षसोंके रहते हुए सर्वप्रथम गणेशकी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17156)
- **Original**: चरणकमलोंका अच्छी तरह प्रक्षालन किया। पूजा कैसे कौ? महाभाग! यह वृत्तान्त मुझसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17157)
- **Original**: तत्पश्चात्‌ वे निराहार रहकर इन्द्रियोंको काबूमें विस्तारपूर्वक वर्णन करनेकी कृपा करें। करके मणिमण्डपमें गयीं। वहाँ उन्होंने श्रीकृष्ण- श्रीनारायण बोले--नारद! तीनों लोकोमें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17158)
- **Original**: प्रातरकी कामनासे उत्तम संकल्पका विधान करके पुण्यवती होनेके कारण पृथ्वी धन्य एबं मान्य है।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17159)
- **Original**: भक्तिपूर्बवक गड्भराजलसे गणेशको स्नान कराया। उस पृथ्वीपर भारतवर्ष कर्मोंका शुभ फल देनेवाला
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17160)
- **Original**: इसके बाद जो चारों वेदों, वसु और लोकोंकी है। उस पुण्यक्षेत्र भारतमें सिद्धाश्रम नामक एक
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17161)
- **Original**: माता, ज्ञानियोंकी परा जननी एवं बुद्धिरूपा हैं; वे महान्‌ पुण्यमय शुभ क्षेत्र है; जो धन्य, यशस्य, पूज्य
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17162)
- **Original**: भगवती राधा श्वेत पुष्प लेकर सामवेदोक्त प्रकारसे और मोक्ष-प्रदाता है। भगवान्‌ सनत्कुमार वहीं
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17163)
- **Original**: अपने पुत्रभूत गणेशका यों ध्यान करने लर्गी। सिद्ध हुए थे। स्वयं ब्रह्माने भी वहीं तपस्या करके “जो खर्व (छोटे कदवाले), लम्बोदर सिद्धि प्राप्त की थी। योगीन्द्र, मुनीद्र, कपिल आदि
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17164)
- **Original**: (तोंदवाले), स्थूलकाय, ब्रह्मतेजसे उद्भासित, सिद्धेन््र और शतक्रतु महेन्द्र वहीं तप करके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17165)
- **Original**: हाथीके-से मुखवाले, अग्निसरीखे कान्तिमान्‌, सिद्धिके भागी हुए हैं। इसी कारण उसे सिद्धाश्रम
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17166)
- **Original**: एकदन्त और असीम हैं; जो सिद्धों, योगियों और कहते हैं। वह सभीके लिये दुर्लभ है। मुने! वहाँ
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17167)
- **Original**: ज्ञानियोंके गुरु-के-गुरु हैं; ब्रह्मा, शिव और शेष गणेश नित्य निवास करते हैं। वहाँ गणेशकी अमूल्य
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17168)
- **Original**: आदि देवेन्द्र, मुनीन्द्र, सिद्धेन्द्र, मुनिगण तथा रत्नोंकी बनी हुई एक सुन्दर प्रतिमा है; जिसकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17169)
- **Original**: संतलोग जिनका ध्यान करते हैं; जो ऐश्वर्यशाली, वैशाखी पूर्णिमाके दिन सभी देवता, नाग, मनुष्य,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17170)
- **Original**: सनातन, ब्रह्मस्वरूप, परम मड्जल, मद्गलके दैत्य, गन्धर्व, राक्षस, सिद्धेन्द्र, मुनीन्द्र, योगीन्द्र और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17171)
- **Original**: स्थान, सम्पूर्ण विष्लोंको हरनेवाले, शान्त, सम्पूर्ण सनकादि महर्षि पूजा करते हैं। उस अवसरपर वहाँ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17172)
- **Original**: सम्पत्तियोंके दाता, कर्मयोगियोंके लिये भबसागरमें पार्वतीके साथ कल्याणकारी शम्भु, गणोंसहित
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17173)
- **Original**: मायारूपी जहाजके कर्णधारस्वरूप, शरणागत- कार्तिकेय और स्वयं प्रजापति ब्रह्मा पधारे
- **Translation**: 

---

