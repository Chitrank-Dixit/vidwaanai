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

### Verse 1 (Vishnu Puran 0.5261)
- **Original**: हे भृगुश्रेष्ठ ! मेरा विचार है कि आप
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5262)
- **Original**: सर्वज्ञ हैं। अतएब आप मनुष्योंके नित्य-नैमित्तिक और काम्य आदि सत्र प्रकारके काका निरूपण कीजिये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5263)
- **Original**: ओर्व बोले--हे राजन्‌! आपने जो नित्य- नैंसेत्तिक आदि क्रियाकलापके धिषयमें पूछा सो मैं सबका वर्णन करता हूँ, एकाग्रचित्त होकर सुनो
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5264)
- **Original**: आ* 10 ] जातस्य जातकर्मादिक्रियाकाण्डमशेषत: । तृतीय अंक्ष 189 पुत्रके उत्पन्न होनेपर पिताको चाहिये कि उसके पुत्रस्य कुर्वीत पिता श्राद्धं चाभ्युद्यात्मकम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5265)
- **Original**: जातकर्म आदि सकल क्रियाकाण्ड और आध्युदयिक युग्मांस्तु प्राद्भुखान्विप्रान्भोजयेन्यनुजेश्वर । यथा वृत्तिस्तथा कुयददियं पित्रय॑ द्विजन्‍्यनाम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5266)
- **Original**: 5 दलक्ला यवैः सबदरैर्पिआ्रान्पिण्डान्मुदा युतः । नान्दीसुखेभ्यस्तीर्थेन दष्यादैवेन पार्थिव
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5267)
- **Original**: 6 प्राजापत्येन वा सर्वमुफ्चारं प्रदक्षिणम्‌। कुर्वीत तत्तथाशेषबृद्धिकालेघषु . भूपते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5268)
- **Original**: 7 ततश्ष नाम कुर्वीत पितैब दशासे5हनि। देवपूर्व नराख्यं हि शर्मवर्मादिसंयुतम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5269)
- **Original**: 8 शर्मेति ब्राह्मणस्योक्त वर्मेति क्षत्रसंश्रयम्‌ । गुप्तदासात्मक॑ नाम प्रशस्तं बैज्यशूद्रयो: । 9 नार्थहीन॑ न चाशास्तं नापश्नब्दयुतं तथा। नामडूल्य जुगुप्य्यं बा नाम कुर्यात्समाक्षरम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5270)
- **Original**: 10 नातिदीर्घ नातिहस्व॑ नातिगुर्वक्षरान्वितम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5271)
- **Original**: सुखोश्चार्य तु तन्नाम कुर्यद्यत्प्रवणाक्षरम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5272)
- **Original**: 19 ततो&नन्तरसंस्कारसंस्कृतों. गुरुवेहमनि । अथोक्तविधिमाभ्रित्य कुर्याद्विद्यापरिग्रहम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5273)
- **Original**: 12 गृहीतकिद्यो गुरवे दत्त्वा च गुरुदक्षिणाम्‌ । गाईस्थ्यमिच्छन्भूपाल॑ कुर्याद्वारपरिग्रहम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5274)
- **Original**: 13 ब्रह्मचर्येण या काल कुर्यात्संकल्पपूर्वकम्‌ । गुरोइ्शुभ्रूषणं कुर्यत्तित्युत्रादेशापि वा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5275)
- **Original**: 14 वैखानसो वापि भवेत्परिब्राडथ वेच्छया । पूर्वसड्डल्पितं यादृक्‌ तादुक्ुर्यान्नराधिप
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5276)
- **Original**: 15 वर्षरेकगुणां. भार्यामुह्रेत्तिगुणस्स्ववम्‌ । नातिकेशञामकेश्ञां वा नातिकृष्णां न पिड्ुलाम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5277)
- **Original**: 16 निसर्गतो5धिकाड़ी वा न्यूनाड्रीपपि नोइहेत्‌ । नाबिशुद्धां सरोमां वाकुलजां वापि रोगिणीम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5278)
- **Original**: 17 न दुष्टों दुष्टवाक्यां वा व्यड्रिनीं पितृमातृतः । न इमश्रुव्यक्षनवर्ती न चैव पुरुषाकृतिम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5279)
- **Original**: 18 श्राद्ध करे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5280)
- **Original**: हे नरेश्वर ! पूर्वाभिमुस्त बिठाकर युग्म ब्राह्मणोंको भोजन कराये तथा द्विजातियोंके व्यवत्तारके अनुसार देव और पितृपक्षकी तृप्तिक छिये श्रारर करे
- **Translation**: 

---

