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

### Verse 1 (Vishnu Puran 0.6121)
- **Original**: यदि किसी अन्य पुरुषके भोजन कसनेसे भी किसी पुरुषकी तृप्ति हो सकती है तो विदेशाको यात्राके समय खाद्चपदार्थ ले जानेका परिश्रम करनेकी क्या आवश्यकता है; पुत्रणण घरपर हो श्राद्ध कर दिया करें
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6122)
- **Original**: अतः यह समझकर कि 'यह (श्राद्धादि कर्मकाष्ड) ल्म्रेगोंकी अन्ध-श्रद्धा ही है' इसके प्रति उपेश्ता करनी चाहिये और अपने श्रेयःसाधनके लिये जो कुछ मैंने कहा है उसमें रुचि करनी चाहिये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6123)
- **Original**: हे अस्तुरगण ! श्रुति आदि आप्तवाक्य कुछ आकादडलसे नहीं गिरा करते । हम, तुम और अन्य सबको भी युक्तियुक्त वाक्‍्योंकों ग्रहण कर लेना चाहिये'
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6124)
- **Original**: अअ* 18 ] तृतीय अंदा 221 त्रीफासर उकाच श्रीपराझरजी बोले--इस प्रकार अनेक युक्तियोंसे मायामोहेन ते दैत्या मायामोहने दैल्यॉको विथलित कर दिया जिससे उनमेंसे व्युत्थापिता न्रयी कश्चिदरोच्वत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6125)
- **Original**: किसीकी भी वेदत्रयीमें रुचि नहीं रहो
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6126)
- **Original**: इस प्रकार चथा नैषां का दैल्यॉके विपरीत सार्गमें प्रकृत्त हो जानेपर देबगण खूब तैयारी इत्थपुन्मार्गयातेषु तेषु दैत्येषु तेईपरा:। उद्योग परम कृत्वा युद्धाय समुपस्थिता:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6127)
- **Original**: 33 ततो दैबासुर॑ युद्धं पुनरेवाभवद्‌ द्विज। हताश्व तेउसुरा देलै: सन्मार्गपरिषन्थिन:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6128)
- **Original**: 34 स्वधर्मकवर्च॑ तेषामभूद्यट्थम॑ द्विज । तेन रक्षाभवत्पूर्व॑ नेशुर्नष्ठें च तत्र ते
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6129)
- **Original**: 35 ततो मैत्रेय तन्यार्गवर्तिनों ये5भवज्ञनाः । नमस्ते तैर्यतस्त्यक्त त्रयीसंवरर्ण तथा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6130)
- **Original**: 36 ब्रह्मचारी गृहस्थश्ष वानप्रस्थस्तथाश्रमी । परित्राड्‌ वा चतुर्थोज्ज्न पञ्ञमो नोपपद्ाते
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6131)
- **Original**: 37 यस्तु सन्त्यज्य गा्हस्थ्यें वानप्रस्थो न जायते । परिव्राद चापि मैत्रेय स नप्म:ः पापकृन्नर:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6132)
- **Original**: 38 नित्यानां कर्मर्णा विप्र तस्य हानिरहर्निशम्‌ । अकुर्वन्विहितं कर्म शक्त: पतति तहिने
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6133)
- **Original**: 39 प्रायक्षित्तेन महता शुद्धिमाप्नोत्यनापदि । पक्ष नित्यक्रियाहाने: कर्त्ता मैत्रेय मानव:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6134)
- **Original**: 40 तस्यावलोकनात्सूयों निरीक्ष्यस्साधुभिस्सदा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6135)
- **Original**: 49 स्पृष्टे स्नानं सचैलस्थ शुद्धेहेतुर्महामते । पुंसो भवति तस्योक्ता न शुद्धि: पापकर्मण:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6136)
- **Original**: 42 देबर्षिपितृभूतानि यस्य निःश्वस्थ वेइमनि। अवान्त्यनचितान्यत्र ल्लेके तस्मान्न पापकृत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6137)
- **Original**: 43 सम्माषणानुप्रश्नादि सहास्यां चेव कुर्वतः । जायते तुल्यता तस्य तेनैव द्विज वत्सरात्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6138)
- **Original**: 44 देवादिनिःश्वासहतं शारीर॑ यस्य खेइम च। न तेन सड्डरं कुर्याद्‌ गृहासनपरिच्छदैः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6139)
- **Original**: 45 अश्व भुड़े गृहे तस्य करोत्यास्यां तथासने । करके उनके पास युद्धके लिये उपस्थित हुए
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6140)
- **Original**: हे ट्विज
- **Translation**: 

---

