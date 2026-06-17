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

### Verse 1 (Sama Ved 0.3561)
- **Original**: . . 1393.पिबा त्व3स्य गिर्वण: सुतस्य पूर्वपा इब । परिष्कृतस्य रसिन इयमासुतिश्चारुर्मदाय पत्थते
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3562)
- **Original**: हे स्तुत्य इन्द्रदेव ! इस शोधित निष्पन्न सोमरस का आप सर्वप्रथम पान करें । यह सोमरस प्रसन्नता बढ़ाने वाले गुणों से युक्त है
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3563)
- **Original**: 1394. आ सोता परि घिज्चताश्व न स्तोममप्तुरं॑ रजस्तुरम्‌। वनप्रक्षमुदप्रुतम्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3564)
- **Original**: हे ऋत्विजो ! अश्व के सदृश वेगपूर्वक जल के प्रवाहक, तेज का विस्तार करने वाले, तैरने वाले सोमरस का शोधन करें और उसका जल में मिश्रण करें
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3565)
- **Original**: 1395. सहस्रधारं वृषभं पयोदुहं प्रियं देवाय जन्मने । ऋछेन य तऋद्रतजातो विवावृधे राजा देव ऋत॑ बृहत्‌
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3566)
- **Original**: उत्तराचिंके ड्ञादजों 5ध्याय- धि 12.8 असंख्य धाराओं से छनित हुआ, सुखवर्द्धक, दुग्ध-मिश्रित प्रिय सोमरस को देवताओं के निमित्त संस्कारित करें । वह दिव्य गुण से युक्त सोम जल से मिलकर वृद्धि पाता है
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3567)
- **Original**: इति द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3568)
- **Original**: के के के
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3569)
- **Original**: तृतीय: खण्ड:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3570)
- **Original**: 1396. अग्निर्वत्राणि जड्घनदद्रविणस्युर्विपन्यया । समिद्ध: शुक्र आहुतः
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3571)
- **Original**: उत्तम प्रकार से दीप्तिमान्‌ और तेजस्वी, हवियों से पुष्ट होने वाले, धन दाता अग्निदेव अज्ञान रूपी शत्रुओं के नाशक हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3572)
- **Original**: 1397. गर्भे मातु: पितुः पिता विदिद्युतानो अक्षरे । सीदचन्बृतस्थ योनिमा
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3573)
- **Original**: पृथ्वी माँ के गर्भ में विशेषरूप से देदीप्यमान एवं अन्तरिक्ष में संरक्षक की भूमिका में नियुक्त अग्निदेव यज्ञ वेदी पर विराजमान हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3574)
- **Original**: 1398. ब्रह्म प्रजावदा भर जातवेदो विचर्षणे । अग्ने यद्दीदयद्धिवि
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3575)
- **Original**: सब कुछ जानने वाले, दिव्य-द्रष्टा, हे अग्निदेव ! अन्तरिक्षलोक में देवों को प्राप्त सुख, ऐश्वर्य और सन्तान आदि से हमें भी सम्पन्न करें
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3576)
- **Original**: 1399. अस्य प्रेषा हेमना पूयमानो देवो देवेभि: समपृकत रसम्‌ । सुतः पवित्र॑ पर्येति रेभन्मितेव सद्य पशुमन्ति होता
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3577)
- **Original**: इस सोम का प्रेरक, स्वर्ण के तुल्य तेज से परिशुद्ध हुआ, दीप्तिमान्‌ सोम देवताओं से मिलता है । ऋत्विज्‌ के पशु आदि से युक्त घरों में प्रविष्ट होने के समान, कूटकर निष्पन्‍्न सोम छनकर पात्रों में प्रवाहित होता है.
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3578)
- **Original**: 1400. भद्गा वस्त्रा समन्या3वसानो महान्कविर्निवचनानि शंसन्‌ । आ वच्यस्व चम्बो: पूथमानो विचक्षणो जागृविददेवबीतौ
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3579)
- **Original**: वीरोचित शौर्य एवं शोभासम्पन्न, महान्‌ ज्ञानी, स्तुत्य, चैतन्य, विशिष्ट द्रष्टा हे सोमदेव ! आप पवित्र होकर यज्ञशाला के पात्रों में प्रविष्ट हों
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3580)
- **Original**: 14091. समु प्रियो मृज्यते सानो अव्ये यशस्तरो यशसां क्षैतो अस्मे । अभि स्वर धन्वा पूयमानो यूयं पात स्वस्तिभि: सदा न:
- **Translation**: 

---

