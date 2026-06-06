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

### Verse 1 (Vishnu Puran 0.4001)
- **Original**: 16 बहन्ति पन्नगा यशक्षैः क्रियते3भीषुसडप्रह: । बालखिल्यास्तथैवैन॑परिवार्य समासते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4002)
- **Original**: 17 नोदेता नास्तमेता च कदाचिच्छक्तिरूपधृक्‌ । विष्णुविष्णो: पृथक्‌ तस्व गणस्सप्तविधोउप्ययम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4003)
- **Original**: 18 स्तप्मस्थदर्पणस्पेत योउयमासन्नतां गतः । छायादर्शनसंयोगं स ते प्राप्नोत्यधात्मनः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4004)
- **Original**: 99 एवं सा वैष्णवी शक्तिनैंबापैति ततो द्विज । मासानुमासं भास्वन्तमध्यास्ते तत्र संस्थितम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4005)
- **Original**: 20 पितृदेबमनुष्यादीन्‍स्स संदाष्याययग्रभुः । परिवर्तत्यहोरात्रकारणं सविता. द्विज
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4006)
- **Original**: 21 सूर्यरश्मि: सुषुम्णा यस्तर्पितस्तेन चन्द्रमा: । कृष्णपक्षेक्मरै: शश्वत्पीयते सै सुधामयः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4007)
- **Original**: 22 पीत॑ ते द्विकलं सोर्म कृष्णपक्षक्षये द्विज । पिबन्ति पितरस्तेषां भास्करात्तर्पणं तथा ।
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4008)
- **Original**: 23 आदते रश्मिभिर्यन्तु क्षितिसंस्थें रसं रवि: । ( आ* 11 यह ऋक्‌-यजु:-सामस्वरूपिणी केदत्रयी भगवान्‌ विष्णुका ही अज्ज है। यह विष्णु-शाक्ति सर्वदा आदित्यमें रहती है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4009)
- **Original**: यह त्रयीमयी वैष्णवी शक्ति केवल सूर्यहीकी अधिष्ठात्री हो, सो नहीं; बल्कि ब्रह्मा, विष्णु और महादेव भी त्रयीमय ही हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4010)
- **Original**: सर्गके आदियें कर्म ऋद्षमय हैं, उसकी स्थितिके समय विष्णु यजुर्मय हैं तथा अन्तकालमें रुद्र साममय हैं। इसीलिये सामगानकी ध्वनि अपबवित्र” मानी गयी है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4011)
- **Original**: इस प्रकार, बह त्रयीमयी सात्विकी वैष्णली सूर्यदेव भी अपनी प्रखर रश्मियॉसे अत्यन्त प्रज्वल्ित होकर संसारके अश्कारको नष्ट कर देते हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4012)
- **Original**: उन मुनिगण स्तुति करते हैं, गन्धर्वगण उनके सम्मुख यशोगान करते हैं। अप्सराएँ नृत्य करती हुई चलती हैं, राक्षस रथके पीछे रहते हैं, सर्पगण रथका साज सजाते हैं और यक्ष घोड़ोंकी बागडोर सैंभाकते हैं तथा बालखिल्यादि रथक्व्रे सन ओरसे घेरे रहते हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4013)
- **Original**: ब्रयीश्क्तिरूप भगवान्‌ विष्णुका न कभी उदय होता है जितना जल तमुत्सूजति भूतानां पुष्टण्थ॑ सस्यवृद्धये
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4014)
- **Original**: 24 कि है उस सबको प्राणियेकत यह और अन्नकी * रुद्के नाशकारी होनेसे उनक्य साम अपवित्र माना गया है अतः सामगानके समय (रातमें) ऋक्‌ तथा यजुरवेंदके अध्ययनका निषेध किया गया है। इसमें गौतमकी स्मृति प्रमाण है--'न सामध्यनादम्यजुषी' अर्थात्‌ सामगानके समय ऋकछ-यजु:का अध्ययन न करे ।
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4015)
- **Original**: 8) हितीय अंश 143 तेन आीणात्यशेघाणि भूतानि भगवात्रवि: । वृद्धिक लिये बरसा देता है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4016)
- **Original**: उससे भगवान्‌ सूर्य पितृदेशभनुष्यादीनेवमाष्याययत्यसा...
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4017)
- **Original**: समस्त प्राणियोंकों आनन्दित कर देते हैं औरइस प्रकार वे देव, पक्षतृप्ति तु देवानां पितृ्णां चैव मासिकीम्‌ । मनुष्य और पितृगण आदि सभीका पोषण करते हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4018)
- **Original**: है मैत्रेय ! इस रीतिसे सूर्यदेश देवताओंकी पाक्षिक, जाश्रत्तप्तिं च मर्त्यानां मैत्रेयार्क: प्रचच्छति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4019)
- **Original**: मासिक तथा मनुष्योंकी नित्यप्रति तृप्ति करते रहते हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4020)
- **Original**: पिला. इति श्रीविष्णुपुराणे ट्वितीयेंडशे एकादशोउध्यायः
- **Translation**: 

---

