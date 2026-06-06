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

### Verse 1 (Sama Ved 0.1261)
- **Original**: 478. प्र सोमासों विपश्चितो5पो नयन्त ऊर्मय: । बनानि महिषा डब
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1262)
- **Original**: बुद्धि की आभवृद्धि करने वाला यह सोमरस, पानी की लहरों के समान तथा स्वाभाविक रूप से पशुओं के बन में जाने के समान, पानी में मिलाया जाता है
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1263)
- **Original**: 479. पबस्वेन्दो वृषा सुत: कृधी नो यशसों जने । विश्वा अप द्विषो जहि
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1264)
- **Original**: है अभिषुत सोम ! आप श्रेष्ठ बल को बढ़ाने वाले हैं । लोगों में हमें यशस्त्री बनाएँ तथा आप हमारे सभी शत्रुओं (विकारों) को नष्ट करें
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1265)
- **Original**: 480. वृषा ह्वासि भानुना द्युमन्तं त्वा हवामहे । पवमान स्वर्द्शम्‌
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1266)
- **Original**: है पवित्र होने वाले, बलवर्द्धछ सोम ! आप सबको समान दृष्टि से देखने वाले तथा तेजस्वी हैं। इस यज्ञ में हम आपको बुलाते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1267)
- **Original**: 489. इन्दु: पविष्ट चेतन: प्रिय: कबीनां मतिः। सृजदश्वं रथीरिव
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1268)
- **Original**: उत्साह की अभिवृद्धि करने वाला, सर्वप्रिय सोमरस ज्ञानी लोगों की स्तुति के साथ, बर्तन में छाना जाता है । रथ का सारथी जिस प्रकार घोड़े को (अपने नियंत्रण में) चलाता है, उसी प्रकार यह सोम पात्र में भरा जाता है
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1269)
- **Original**: 482. असक्षत प्र बाजिनों गव्या सोपासों अश्वया। शुक्रासो वीरयाशवः
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1270)
- **Original**: । बल और स्पूर्ति बढ़ाने वाला यह सोमरस तेजस्वी है । गाय, घोड़े तथा वीर पुत्रों की कामना करने वालों के द्वारा अभिषुत किया जाता है । जो साधक इसका अभिषवण (निचोड़ना) करते हैं, यह उनकी गाय, घोड़े, बीरपत्र आदि कामनाओं की पूर्ति करता है
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1271)
- **Original**: 483. पवस्व देव आयुषगिन्द्रं गच्छतु ते मदः । वायुमा रोह धर्मणा
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1272)
- **Original**: है दिव्य गुण वाले सोम ! आप छनने के लिए पात्र में जाएँ। आपका आनन्ददायी रस इद्धदेव को प्राप्त हो । आप दिव्यरूप से वायु में मिल जाएँ
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1273)
- **Original**: « 484.पबमानो अजीजनद्विवश्चित्रं न तन्यतुम्‌। ज्योतिर्वैश्वानर॑ बृहत्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1274)
- **Original**: पवित्र होने के बाद इस सोमरस ने दिव्यलोक में विद्यपान, सबको प्रकाशित करते में समर्थ, महान्‌ बैश्वानर ज्योति को बिजली के समान प्रकट किया
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1275)
- **Original**: 485. परि स्वानास इन्दवो मदाय ब्हणा गिरा। मधो अर्पन्ति धारया
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1276)
- **Original**: पूर्वार्चिकि पावमानपर्वणि पञ्चमो ध्याय: 5.3 अभिषुत होने (निचोड़ने) के बाद अप्ृत स्वरूप, ज्ञानवर्द्धक, मधुरसोम साथकों के द्वारा स्तुतिगान करत हुए छना जाता है
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1277)
- **Original**: 486.परि प्रासिष्यदत्कवि: सिन्धोरूर्मावधि श्रित: । कारूुं बिश्रत्पुरुस्पृहम्‌
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1278)
- **Original**: बुद्धिवर्द्धक, प्रशंसनीय, याजकों का पोषण करने वाला, नदी की लहरों (जल) में मिला हुआ, यह सोम, पात्र (सत्पात्र) में स्थिर होता है
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1279)
- **Original**: इति द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1280)
- **Original**: के के के
- **Translation**: 

---

