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

### Verse 1 (Sama Ved 0.3401)
- **Original**: 1327. तव द्र॒प्सा उदप्रुत इन्द्र मदाय वावृधुः ।त्वां देवासो अमृताय क॑ पपु:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3402)
- **Original**: (है सोम !) जल में मिश्रित किया जाने वाला आपका रस, इन्द्रदेव के आनन्द एवं यश को बढ़ाने के लिए है । देवगण अमरत्व प्राप्त करने हेतु आपका पान करते हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3403)
- **Original**: 1328. आ न: सुतास इन्दवः पुनाना धावता रयिम्‌ वृष्टिद्यावों रीत्याप: स्वर्विद:।
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3404)
- **Original**: :च' आकाश से प्राण-पर्जन्य की वृष्टि कराने वाले, शोधित होकर रसरूप निष्पन हुए हे दिव्य सोमरंस ! आप हमें श्रेष्ठ ऐश्वर्य प्रदान करें
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3405)
- **Original**: 1329. परि त्यं हर्यतं हरिं बश्लुं पुनन्ति वारेण । यो देवान्विश्वाँ इत्परि मदेन सह गच्छति
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3406)
- **Original**: हम मनभावक, पापनाशक, कान्तिमान्‌ सोम को छन्ने से शोधित करते हैं । वह सोमरस सब देवों को हर्षयुक्त रसों सहित प्राप्त होता है
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3407)
- **Original**: 1330. द्विय॑ पञ् स्ववशसं सखायो अद्विसं हतम्‌ । प्रियमिन्द्रस्य काम्य॑ प्रस्नापयन्त ऊर्मय:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3408)
- **Original**: पाषाणों द्वारा कूटकर निष्पल, कौर्तिवान्‌ सबका इष्ट और इन््रदेव के प्रिय सोमरस को दसों अँगुलियाँ भलीप्रकार शोधित करती हैं और जल से युक्त करती हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3409)
- **Original**: 1339. इन्द्राय सोम पातवे वृत्रध्ने परि षिच्यसे । नरे च दक्षिणावते वीराय सदनासदे
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3410)
- **Original**: हे सोमरस ! दुष्टनाशक इन्द्रदेव के पान के लिए, यज्ञ में दक्षिणा देने वाले वीर के लिए और यज्ञ करने वाले यजमान के लिए आप पात्र में प्रवाहित होकर स्थिर हों
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3411)
- **Original**: 1332. पवस्व सोम महे दक्षायाश्रो न निक्‍्तो वाजी धनाय
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3412)
- **Original**: है सोमरस ! अश्व के समान वेगवान्‌ जल से धोकर शुद्ध हुए आप शत्रुनाशक बल और ऐश्वर्य के लिए पात्र में आएँ
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3413)
- **Original**: . 3333. प्र ते सोतारों रसं मदाय पुनन्ति सोम॑ महे द्युम्माय
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3414)
- **Original**: है सोमदेव ! साधकगण आपके रस को आनन्दवृद्धि के लिए शोधित करते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3415)
- **Original**: 1334. शिशु जज्ञानं हरिं मृजन्ति पवित्रे सोम॑ देवेभ्य इन्दुम्‌
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3416)
- **Original**: नवजात शिशु को शुद्ध करने के सदृश ऋषत्विग्गण, हरिताभ, दीप्तिवान्‌ सोम को देवों के निमित्त छन्ने से शोधित करते हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3417)
- **Original**: 1335. उपो घु जातमप्तुरं गोभिर्भड़ं परिष्कृतम्‌ । इन्दुं देवा अयासिषु:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3418)
- **Original**: शत्रुनाशक, जल-गोदुग्धादि में मिश्रित, संस्कारित, दीप्तिमान्‌ सोमरस का देवगण पान करते हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3419)
- **Original**: उत्तराचिंके दशमो 5 ध्याय- 10.11 1336. तमिद्वर्धन्तु नो गिरो वत्सं संशिश्वरीरिव। यइन्द्रस्य हद सनि:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3420)
- **Original**: 14 हमारी वाणी इन्द्रदेव के हार्दिक प्रिय पात्र, श्रेष्ठ सोम की स्तुतियाँ करें । जिस प्रकार बालक को माता अपने दुग्ध से पुष्ट करती है, उसी प्रकार हमारी स्तुतियाँ सोम की यशवृद्धि करें
- **Translation**: 

---

