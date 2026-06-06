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

### Verse 1 (Vishnu Puran 0.9701)
- **Original**: वर्षा और जायुके बेगपूर्वक चलते रहनेसे गौओंफे कटि, जैघा और ग्रीवा आदि सुत्र हो गये और काँपते- कॉँपते अपने प्राण छोड़ने लगीं [ अर्थात्‌ मूच्छित हो गयीं ]
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9702)
- **Original**: है महाम्‌ने ! कोई गौएँ तो अपने बछड़ोंको अपने नोथे छिपाये खड़ी रहीं और कोई जलके वेगसे बत्सहीना हो गयीं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9703)
- **Original**: वायुसे काँपते हुए दीनवदन बछड़े मानो व्याकुल होकर मन्द स्वस्से कृष्णचन्द्रसे रक्षा करो, रक्षा करो' ऐसा कहने लगे। 12
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9704)
- **Original**: बेड4ड0 श्रीचिष्णुपुराण [ अब् 61 ततस्तज्ञेकुले सर्व गोगोपीगोपसडुलम्‌ अतीवात्त॑ हरिदृष्ठा मैत्रेयाचिन्तयत्तदा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9705)
- **Original**: 13 एतत्कृत॑ महेन्द्रेण मखभड्भविरोधिना। तदेतदखिर्ल॑ गोष्ठ॑ त्रातव्यमधुना मया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9706)
- **Original**: 14 इममद्रिमह॑ थैयदित्पाट्योरुशिलाधघनम्‌ । धारबिष्यामि गोष्ठस्प पृथुच्छश्नमिवोपरि
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9707)
- **Original**: 15 श्रीपराझर उबाच इति कृत्या मरतिं कृष्णो गोवर्धनमहीधरम्‌। उत्पास्यैककरेणैव धारयामास लीलया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9708)
- **Original**: 16 गोपांश्राह हसउ्छौरिस्समुत्पाटितभूधर: । विश्वध्वमत्र त्वरिता: कृतं वर्षनिवारणम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9709)
- **Original**: 17 सुनिवातेषु देशेषु यथा जोषमिहास्यताम्‌। प्रतिश्यतां न भेतव्य॑ गिरिपाताश्व निर्भय:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9710)
- **Original**: 18 इत्युक्तास्तेन ते गोपा विविशुर्गोधनैस्सह । जकटारोपितैर्भाण्डैगोप्यश्वासारपीडिता:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9711)
- **Original**: 19 कृष्णो5पि ते दधारैबव दैलमत्यन्तनिश्चलम्‌ । ब्रजेकवासिभिह॑र्षविस्मिताक्षै्निरीक्षित:.
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9712)
- **Original**: 20 गोपगोपीजनैईए्टे: प्रीतिविस्तारितिक्षणै: । संस्तृयमानचरित:. कृष्णइश्नैलमधारयत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9713)
- **Original**: 29 सप्तरात्र महामेघा. बवर्धुनन्दगोकुले । इन्द्रेण चोदिता विप्र गोपानां नाशकारिणा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9714)
- **Original**: 22 ततो धृते महाहौले परित्राते च गोकुले। बलभिद्वारयामास तान्धनान्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9715)
- **Original**: 23 व्यश्रे नभसि देवेन्रे वितथात्मवचस्यथ । निष्क्रम्य गोकुलं हुं स्वस्थानं पुनरागपत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9716)
- **Original**: 24 मुमोच्र कृष्णो<पि तदा गोवर्धनमहाचलम्‌ । विस्मितमुखर्दष्टस्तैस्तु ब्रजौकसे:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9717)
- **Original**: 25 हे मैत्रेय ! उस समय गो, गोपी और गोपगणके सरि सम्पूर्ण गोकुलको अल्पन्त व्याकुछ देखकर श्रीहरिने विचारा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9718)
- **Original**: यज्ञ-भंगके कारण विरोध मानकर यह सन करतूत इन्द्र हो कर रहा है; अतः अब मुझे सम्पूर्ण त्रजकी रक्षा करनी चाहिये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9719)
- **Original**: अब मैँ धैर्यपूर्वक बड़ी-बड़ो शिल्प्रओंसे घनीभूत इस पर्वतको उखाड़कर इसे एक बड़े छत्रफे समान ब्रजके ऊपर धारण करूँगा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9720)
- **Original**: श्रीपराशरजी खोले--श्रीकृष्णचन्द्रन. ऐसा विचारकर गोवर्धनपर्वतको उखाड़ लिया और उसे लील्ासे ही अपने एक हाथपर उठा ल्िया
- **Translation**: 

---

