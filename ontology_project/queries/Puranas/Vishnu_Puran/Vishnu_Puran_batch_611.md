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

### Verse 1 (Vishnu Puran 0.12201)
- **Original**: पन्द्रह कला नाडिका तु प्रमाणेन सा कल्ठा दश पञ्च च । एक नाडिकाका प्रमाण है। वह नाडिका साढ़े बारह पल उन्पानेनाण्मसस्सा तु ॒ पलान्यर्द्धतयोदश
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12202)
- **Original**: तंबैके बने हुए जलके पात्नसे जानी जा सकतो है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12203)
- **Original**: के जायुपुराणमें इन अठारह संख्याओंके इस प्रकार नाम हैं--एक, दस, शत, सहख, अयुत, नियुत, प्रयुत, अर्जुद, न्यबुद, वृन्द, स्॒र्ब, निखर्न, शंख, पद्म, समुद्र, मध्य, अन्त, परार्ड ।
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12204)
- **Original**: आत्3 ] मागधेन तु समानेन जलग्रस्थस्तु स स्मृतः । हेममाषै: .. कृतच्किद्रश्नतुर्भिश्रतुरदुलैः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12205)
- **Original**: 8 नाडिकाभ्यामथ द्वाभ्यां मुहूर्तों द्विजसत्तम । अहोरात्र॑ मुहूर्तास्तु त्रिंशन्‍्मासों दिनैस्तथा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12206)
- **Original**: 9 चतुर्युगसहस््र॑ तु कथ्यते ब्रह्मणो दिनम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12207)
- **Original**: 11 स॒ कल्पस्तनत्र मनवशततुर्दश महामुने । तदन्ते चैब मैत्रेय ब्राह्मो नैसिप्तिकों छयः ।
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12208)
- **Original**: 12 तस्य स्वरूपमत्युग्र॑ मैत्रेय गदतो मम । श्रृणुष्ठ प्राकृत भूयस्तव वक्ष्याम्यहै छूयम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12209)
- **Original**: 13 चतुर्युगसहस्नान्ते क्षीणप्राये महीतले । अनाबृष्टिस्तीबोग्मा जायते शतवार्षिकी
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12210)
- **Original**: 14 ततो यान्यल्पसाराणि तानि सत्त्वान्यशेषत: । क्षयं॑ यान्ति मुनिश्रेष्ठ पार्थिवान्यनुपीडनात्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12211)
- **Original**: 15 ततः स भगवान्विष्णू रुद्रूपधरो5व्यय: । क्षयाय यतते कर्तुमात्मस्थास्सकला: प्रजा:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12212)
- **Original**: 16 ततस्स भगवान्विष्णुर्भानोस्सप्तसु रहिमषु। स्थितः पिवत्यशेषाणि जलानि मुनिसत्तम
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12213)
- **Original**: 17 पीत्वाम्भांसि समस्तानि प्राणिभूमिगतान्यपि । शोष॑ नयति मैत्रेय समस्त पृथिवीतलम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12214)
- **Original**: 98 समुद्रानस्सरित: शौलनदीप्रस्नवणानि च। पातालेषु च॒ यत्तोय॑ तत्सर्व नयति क्षयम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12215)
- **Original**: 19 ततस्तस्यानुभावेन. तोयाहारोपबृंहिता: । त एवं रहमयस्सप्त जायन्ते सप्त भास्करा:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12216)
- **Original**: 20 अधश्षोध्व॑ च ते दीप्रास्ततस्सप्त दिवाकरा: । दहन्यशेष॑ त्रैलोक्य॑ सपातालतलं द्विज
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12217)
- **Original**: 21 दहामान तु तैर्दीपित्लैलोक्य॑ द्विज भास्करैः । साद्रिनद्र्णाभोगं॑ निरत्रेहमभिजायते
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12218)
- **Original**: 22 ततो निर्दग्धवृक्षाम्तरु अलोक्यमखिलं द्विज । भवत्येषा च्॒ वसुधा कूर्मपृष्ठोपमाकृति:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12219)
- **Original**: 23 घष्ठ अंडा 439 मगधरदेज्ञीय मापसे वह पात्र जलप्रस्थ कहत्मता है; उसमें चार अक्लुल लम्बी चार मासेकी सुवर्ण-पास्प्रकासे छिद्र किया रहता है [ उसके छिद्धकों ऊपर करके जलमें डुबो देनेसे जितनी देरमें वह पात्र भर जाय उतने ही समयको एक नाडिका समझना चाहिये ]
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12220)
- **Original**: हे द्विजसत्तम ! ऐसी दो नाडिकाओंक्य एक मुहूर्त होता है, तीस मुहूर्तका एक दिन-रात होता है तथा इतने (तीस) ही दिन-रातका एक मास होता है
- **Translation**: 

---

