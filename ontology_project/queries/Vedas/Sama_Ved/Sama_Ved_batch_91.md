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

### Verse 1 (Sama Ved 0.1801)
- **Original**: 696. अस्येदिन्द्रो मदेष्वा ग्राभं गृष्णाति सानसिम्‌ । _ बज्र॑ च वृषणं भरत्समप्सुजित्‌
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1802)
- **Original**: सेवन योग्य सोमपान से आनन्दित हुए इन्द्रदेव जल प्रवाह को स्तम्भित करके अपने धनुष और वज्र को धारण कर लेते हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1803)
- **Original**: 697.पुरोजिती वो अन्धसः सुताय मादयिलवे
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1804)
- **Original**: अप श्वान॑ श्नधिष्टन सखायो दीर्घजिह्ययम्‌
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1805)
- **Original**: हे स्तोताओ ! निश्चित रूप से विजय दिलाने वाले, आनन्ददायक इस सोमरस को श्वान (वृत्तिवालों) से बचाओ
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1806)
- **Original**: 698.यो धारया पावकया परिप्रस्यन्दते सुतः । इन्दुरश्वो न कृत्व्य:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1807)
- **Original**: यज्ञ में सहयोगी यह सोमरस शोधित होते समय अश्व वेग जैसी गति से पात्र में गिरता है
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1808)
- **Original**: 699.त॑ दुरोषमभी नर: सोम॑ विश्वाच्या धिया। यज्ञाय सन्त्वद्रय:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1809)
- **Original**: हे क्गरत्विजो ! दुष्टगाशक उस सोम को आवाहित करो और यज्ञ का सम्मान करते हुए मानव- मात्र के कल्याण की कामना करो
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1810)
- **Original**: 4100 700.अभि प्रियाणि पवते चनोहितो नामानि यद्»ो अधि येषु वर्धते । आ सूर्यस्य बृहतो बृहन्नधि रथं विष्वज्षमरुहद्विचक्षण:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1811)
- **Original**: तृप्तिदायी जल को पवित्र करने वाला, हितकारी सोम, जिस जल में मिलाया जाता है, उसमें यह महान्‌ और सर्वज्ञ सोमरस सूर्य के प्रकाश से अधिक प्रखर हो उठता है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1812)
- **Original**: 701.ऋतस्य जिड्ला पवते मधु प्रियं वक्ता पतिर्धियो अस्या अदाभ्य:। दाति पुत्र: पित्रोरपीच्यां3नाम तृतीयमधि रोचन॑ दिव:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1813)
- **Original**: यज्ञ की जिह्ला सदृश, छाने जाते समय शब्द करता हुआ यह सोमरस प्रिय और मधुर रूप में तैयार होता है । यज्ञ कार्य का रक्षक यह सोम अभय है । माता-पिता के नाम से अपरिचित, यजमान द्वारा तैयार किया गया, लोक-लोकान्तरों में ख्यातिसिद्ध यह सोम तीसरी संज्ञा (सोमजयी के रूप में) धारण करता है
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1814)
- **Original**: 702. अब द्युतान: कलशाँ अचिक्रदन्नभियेंमाण: कोश आ हिरण्यये । अभी ऋजतस्य दोहना अनूषताधि त्रिपृष्ठ उघसो वि राजसि
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1815)
- **Original**: उत्तराचिकि प्रवमो5ध्याय- 17 ऋत्विग्गण स्वर्ण कलश में शोधित होते समय, शब्द करने वाले तेजस्वी सोमरसत की स्तुति करते हैं । यह सोम तीनों ही संध्याओं (प्रात: मध्याह, साय) में प्रकाशित होता है
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1816)
- **Original**: इति पश्चम: खण्ड:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1817)
- **Original**: के के के
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1818)
- **Original**: पषष्ठ: खण्ड:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1819)
- **Original**: 703. यज्ञायज्ञा वो अग्नये गिरागिरा च दक्षसे । प्रप्न बयममृतं जातवेदसं प्रियं मित्र न शंसिषम्‌
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1820)
- **Original**: हे प्रार्थना करने वाले साधको ! आप प्रत्येक यज्ञ में प्रज्जलित अग्निदेय की अपनी वाणी से स्तुति करो । हम भी उन अविनाशो, सर्वज्ञ अग्निदेव की, सखा के समान प्रशंसा करते हैं
- **Translation**: 

---

