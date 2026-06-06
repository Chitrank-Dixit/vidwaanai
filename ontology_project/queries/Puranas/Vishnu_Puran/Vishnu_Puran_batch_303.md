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

### Verse 1 (Vishnu Puran 0.6041)
- **Original**: 218 तमूचुस्सकला देवा: प्रणिपातपुरस्सरम्‌। अ्रीविष्णुपुराण ( अब् 18 उन्हें देखकर समस्त देवताओंने प्रणाम करनेके अ्रसीद नाथ दैत्येभ्यख्राहि नश्शरणार्थिन:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6042)
- **Original**: अन्तर उनसे कहा--हे नाथ ! प्रसन्न होइये और हम त्रैलोक्ययज्ञभागाश्च॒ दैत्वैर्लादपुरोगमै: । हता नो ब्रह्मणो5प्याज्ञामुल्लजूय परमेश्वर
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6043)
- **Original**: 37 यहाप्यशेषभूतस्य वर्य॑ ते च तवांशजा: । तथाप्यविद्याभेदेन भिन्न॑ पश्यामहे जगत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6044)
- **Original**: 38 स्ववर्णधर्माभिरता. वेदपार्गानुसारिण: । न शक्यास्तेउरयो हन्तुमस्माभिस्तपसावृता:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6045)
- **Original**: 39 तपमुपायमशेषात्मन्नस्मारक दातुपईसि । येन तानसुरानहन्तुं भवेम भगवन्क्षपा:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6046)
- **Original**: 40 श्रीपद॒शर उवाच इत्युक्तो भगवांस्तेभ्यो मायामोह शरीरतः । समुत्पाद्य ददौ बिष्णु: प्राह चेदं सुरोत्तमान्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6047)
- **Original**: 49 मायामोहो5यमखिलान्दैत्यांस्तान्मोहयिष्यति । ततो वध्या भविष्यन्ति वेदमार्गबहिष्कृता:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6048)
- **Original**: 42 स्थित स्थितस्य पे वध्या यावन्त: परिपन्धिन: । ब्रह्मणो हाधिकारस्य देवदैत्यादिका: सुरा:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6049)
- **Original**: 43 तद्गव्छत न भी: कार्या मायामोहोउयमग्रत: । गच्छन्नद्योपकाराय भवतां भव्रिता सुरा:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6050)
- **Original**: 44 औपराशर उताच इत्युक्ता प्रणिपत्वैन॑ यवुर्देवा यथागतम्‌। मायामोहो5पि तैस्सार्द ययौ यत्र महासुरा:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6051)
- **Original**: 45 अरणागतोंकी दैल्योंसे रक्षा कीजिये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6052)
- **Original**: है परमेश्वर ! हाद प्रभृति दैत्यगणने बद्याजोकी आज्ञाका भी उल्लद्लून कर हमारे और ज़िल्लेकीके यज्ञभागोंका अपहरण कर लिया है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6053)
- **Original**: यहापि हम और बे सर्वभूत आपहीके अंदाज हैं तथापि अखिद्यावश हम जगतक्पे परस्पर भिन्न-भिन्न देखते हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6054)
- **Original**: हमारे शत्रुगण अपने वर्णधर्मका पालन करनेवाले, वेदमार्गावरूप्णी और तपोनिष्ठ हैं, अतः ले हमसे नहीं मारे जा सकते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6055)
- **Original**: अतः हे सर्वात्मन्‌ ! जिससे हम उन असुरोंका वध करनेमें समर्थ हों ऐसा कोई उपाय आप हमें बतलाइये''
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6056)
- **Original**: ओऔपराहारजी जोस्के--उगके ऐसा कहनेपर भगवान्‌ विष्णु ने अपने शरीरसे मायामोहको उत्पन्न किया और उसे देवताओंको देकर कहा--
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6057)
- **Original**: “यह मायामोह उन सम्पूर्ण दैत्यगणकों मोहित कर देंगा, तब वे वेदमार्गका उल्लड्डन करनेसे तुमलोगोंसे मारे जा सकेंगे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6058)
- **Original**: हे देखगण ! जो कोई देवता अथवा दैत्य ब्रह्माजीके कार्यमें बाघा डालते हैं वे सृष्टिकी रक्षामें तत्पर मेरे वध्य होते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6059)
- **Original**: अतः हे देवगण
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6060)
- **Original**: अब तुम जाओ। डरे मत। यह मायामोह आगेसे जाकर तुम्हारा उपकार करेगा"
- **Translation**: 

---

