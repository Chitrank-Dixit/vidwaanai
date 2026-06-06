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

### Verse 1 (Bramha 0.3421)
- **Original**: कामधेनु गौ जगन्माता सुरभिने ननन्‍्दीसे सब हाल 'नन्दिकेश्व! तुम गरुड़के साथ ही नागको
- **Translation**: 

---

### Verse 2 (Bramha 0.3422)
- **Original**: कहा। नन्‍्दीने भी खिन्न होकर भगवान्‌ शंकरको महादेवजीके पास ले जाओ।' “बहुत अच्छा' कहकर
- **Translation**: 

---

### Verse 3 (Bramha 0.3423)
- **Original**: सब बातें बतायां। तब शंकरजीने नन्‍्दीसे नन्दी गरुड़ और नागके साथ धीरे-धीरे शंकरजीके । कहा--' तुम्हारी प्रत्येक बात सिद्ध हो।' पास गये और सब समाचार उन्हें कह सुनाया।
- **Translation**: 

---

### Verse 4 (Bramha 0.3424)
- **Original**: महादेवजीकी यह आज्ञा पाकर नन्दीने समस्त तब शंकरजीने गरुड़से कहा--'महाबाहो! तुम
- **Translation**: 

---

### Verse 5 (Bramha 0.3425)
- **Original**: गोजातिको अपनेमें समेट लिया। स्वर्गलोक और लोकपावनी गौतमी गज़ाके पास जाओ। वे समस्त
- **Translation**: 

---

### Verse 6 (Bramha 0.3426)
- **Original**: शरर्यलोककी समस्त गौएँ अदृश्य हो गयीं। तब अभीष्ट बस्तुओंको देनेवाली हैं। उस शान्तिमयी । देवताओंने मेरे पास आकर कहा-- भगवन्‌! सरितामें स्नान करलेसे तुम्हें समस्त इच्छित वस्तुएँ, दिया सौगुनी अथवा सहस्रगुनी होकर मिलेंगी। गरुड़!
- **Translation**: 

---

### Verse 7 (Bramha 0.3427)
- **Original**: जो सब प्रकारके पापोंसे सन्तप्त हैं, दुर्दैदसे जिनका उद्योग नष्ट हो गया है, उतर प्राणियोंके लिये भनोवाज्छित फल देनेबाली गोदावरी नदी ही शरण
- **Translation**: 

---

### Verse 8 (Bramha 0.3428)
- **Original**: हैं।' भगवान्‌ शिवकी यह बात सुनकर गरुड़ प्रणाम करके चले गये। गोदावरीके तटपर पहुँचकर उन्होंने
- **Translation**: 

---

### Verse 9 (Bramha 0.3429)
- **Original**: जलमें स्तान किया और भगवान्‌ शिव तथा विष्णुके
- **Translation**: 

---

### Verse 10 (Bramha 0.3430)
- **Original**: अरणोंमें मस्तक झुकाया। फिर उनमें पूर्ववत्‌ वेग
- **Translation**: 

---

### Verse 11 (Bramha 0.3431)
- **Original**: आ गया और ये उड़कर भगवान्‌ विष्णुके समीप
- **Translation**: 

---

### Verse 12 (Bramha 0.3432)
- **Original**: चले गये। तबसे वह समस्त अभीष्ट बस्तुओंको
- **Translation**: 

---

### Verse 13 (Bramha 0.3433)
- **Original**: देनेवाला तीर्थ 'गारुड़तीर्थ' के नामसे प्रसिद्ध हुआ।
- **Translation**: 

---

### Verse 14 (Bramha 0.3434)
- **Original**: बत्स नारद! मनुष्य मन और इन्द्रियोंकों संयममें रखते हुए वहाँ स्तरान आदि जो भी कर्म करता है, ।
- **Translation**: 

---

### Verse 15 (Bramha 0.3435)
- **Original**: * ब्ैततीर्थ, शुक्रतीर्थ और इद्धतीर्थका माहात्म्य * 165 गौओंके बिना जीवन नहीं रह सकता।' उस
- **Translation**: 

---

### Verse 16 (Bramha 0.3436)
- **Original**: बोले--' आपलोग गो-यज्ञ कीजिये, तभी दिव्य समय मैंने देवताओंसे कहा-'जाओ, भगवान्‌
- **Translation**: 

---

### Verse 17 (Bramha 0.3437)
- **Original**: और मानस गौएँ प्राप्त होंगी।' तत्पश्चात्‌ गौतमी शंकरसे याचना करो।' तदनन्तर उन्होंने भगवान्‌
- **Translation**: 

---

### Verse 18 (Bramha 0.3438)
- **Original**: गड्भाके तटपर देवताओंने गोयज्ञका आयोजन शंकरकी स्तुति करके उनसे सब हाल कहा।
- **Translation**: 

---

### Verse 19 (Bramha 0.3439)
- **Original**: किया। फिर वहाँसे गौएँ बढ़ने लगीं। तभीसे महादेवजीने भी देवताओंको उत्तर दिया--'इस
- **Translation**: 

---

### Verse 20 (Bramha 0.3440)
- **Original**: वह तीर्थ 'गोवर्धन' नामसे प्रसिद्ध हुआ। वह विषयमें ननन्‍दी जानते हैं।' तब सब देवता
- **Translation**: 

---

