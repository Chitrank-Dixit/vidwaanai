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

### Verse 1 (Bhagwat_Geeta 7.684)
- **Original**: एतद्योनीनि भूतानि सर्वाणीत्युपधारय। अहं कत्स्नस्य जगत: प्रभवः प्रलयस्तथा
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 7.685)
- **Original**: 100 * श्रीमद्धगवद्रीता * हे अर्जुन! तू ऐसा समझ कि सम्पूर्ण भूत इन दोनों प्रकृतियोंसे ही उत्पन्न होनेवाले हैं और मैं सम्पूर्ण जगत्‌का प्रभव तथा प्रलय हूँ अर्थात्‌ सम्पूर्ण जगत्‌का मूलकारण हूँ
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 7.686)
- **Original**: मत्त: परतरं नान्यत्किल्लिदस्ति धनक्जय। मयि सर्वमिदं प्रोत॑ सूत्रे मणिगणा इव
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 7.687)
- **Original**: हे धनझ्जय! मुझसे भिन्न दूसरा कोई भी परम कारण नहीं है। यह सम्पूर्ण जगतू सूत्रमें सूत्रके मनियोंके सदृश मुझमें गुँथा हुआ है
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 7.688)
- **Original**: रसो5हमप्सु कौन्तेय प्रभास्मि शशिस्‌र्ययो: । प्रणव: सर्ववेदेषु शब्द: खे पौरुषं नृषु
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 7.689)
- **Original**: हे अर्जुन! मैं जलमें रस हूँ, चन्द्रमा और सूर्यमें प्रकाश हूँ, सम्पूर्ण बेदोंमें ओंकार हूँ, आकाशमें शब्द और पुरुषोंमें पुरुषत्व हूँ
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 7.690)
- **Original**: पुण्यो गन्ध: पृथिव्यां च तेजश्रास्मि विभावसौ । जीवन सर्वभूतेषु तपश्चास्मि तपस्विषु
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 7.691)
- **Original**: मैं पृथ्वीमें पवित्र* गन्ध और अग्निमें तेज हूँ * शब्द, स्पर्श, रूप, रस, गन्धसे इस प्रसड्भमें इनके कारणरूप तन्मात्राओंका ग्रहण है, इस बातको स्पष्ट करनेके लिये उनके साथ पवित्र शब्द जोड़ा गया है।
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 7.692)
- **Original**: * अध्याय 7% 101 तथा सम्पूर्ण भूतोंमें उनका जीवन हूँ और तपस्वियोंमें तप हूँ
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 7.693)
- **Original**: बीजं मां सर्वभूतानां विदिद्वि पार्थ सनातनम्‌। बुद्धद्विर्बुस्द्विमतामस्मि तेजस्तेजस्विनामहम्‌
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 7.694)
- **Original**: । हे अर्जुन! तू सम्पूर्ण भूतोंका सनातन बीज मुझको ही जान। मैं बुद्धिमानोंकी बुद्धि और तेजस्वियोंका तेज हूँ
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 7.695)
- **Original**: बल॑ बलवतां चाहं कामरागविवर्जितम्‌। धर्माविरुद्धों भूतेषु कामोउस्मि भरतर्षभ
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 7.696)
- **Original**: हे भरतश्रेष्ठ! मैं बलवानोंका आसक्ति और कामनाओंसे रहित बल अर्थात्‌ सामर्थ्य हूँ और सब भूतोंमें धर्मके अनुकूल अर्थात्‌ शास्त्रके अनुकूल काम हूँ
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 7.697)
- **Original**: ये चैव सात्त्विका भावा राजसास्तामसाश्च ये। मत्त एवेति तान्विद्द्रि न त्वहं तेषु ते मयि
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 7.698)
- **Original**: और भी जो सत्त्वगुणसे उत्पन्न होनेवाले भाव हैं और जो रजोगुणसे तथा तमोगुणसे होनेवाले भाव हैं, उन सबको तू “मुझसे ही होनेवाले हैं ' ऐसा जान, परन्तु वास्तवमें * उनमें मैं और वे मुझमें नहीं हैं
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 7.699)
- **Original**: + गीता अ0 9 श्लोक 4-5 में देखना चाहिये।
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 7.700)
- **Original**: 102 * श्रीमद्धगवद्रीता * त्रिभिर्गुणमयैर्भावरेभि: सर्वमिदं जगत्‌। मोहितं नाभिजानाति मामेभ्य: परमव्ययम्‌
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 7.701)
- **Original**: गुणोंके कार्यरूप सात्तिवक, राजस और तामस-- इन तीनों प्रकारके भावोंसे यह सारा संसार-- प्राणिसमुदाय मोहित हो रहा है, इसीलिये इन तीनों गुणोंसे परे मुझ अविनाशीको नहीं जानता
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 7.702)
- **Original**: दैवी होषा गुणमयी मम माया दुरत्यया। मामेव ये प्रपद्यन्ते मायामेतां तरन्ति ते
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 7.703)
- **Original**: क्योंकि यह अलौकिक अर्थात्‌ अति अद्भुत त्रिगुणमयी मेरी माया बड़ी दुस्तर है; परन्तु जो पुरुष केवल मुझको ही निरन्तर भजते हैं, वे इस मायाको उल्लंघन कर जाते हैं अर्थात्‌ संसारसे तर जाते हैं
- **Translation**: 

---

