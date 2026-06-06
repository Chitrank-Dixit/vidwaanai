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

### Verse 1 (Vaivtpuran 6.9251)
- **Original**: लगीं। 'गोपो और गोपियो! तुम भूतलपर श्रेष्ठ तरह नष्ट हो जाते हैं, जैसे प्रज्वलित अग्रिमें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.9252)
- **Original**: गोपोंके शुभ घर-घरमें जन्म लो।' श्रीकृष्णकी तिनके। जब मैं उनका घातक बनकर उपस्थित
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.9253)
- **Original**: यह बात पूरी होते ही वहाँ सब लोगोंने देखा, होता हूँ, तब कोई भी उनकी रक्षा नहीं कर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.9254)
- **Original**: एक उत्तम रथ (विमान) आ गया। वह श्रेष्ठ पाताँ। देवताओ! मैं पृथ्वीपर जाऊँगा। अब
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.9255)
- **Original**: मणिरत्रोंके सारतत्त्व तथा होरकसे विभूषित था। तुमलोग भी अपने स्थानको पधारो और शीघ्र ही
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.9256)
- **Original**: लाखों श्वेत चँचर तथा दर्पण उसकी शोभा बढ़ा *अहं प्राणाश्ष भक्तानां भक्ता: प्राणा मम्रापि च॒ । ध्यायन्ति ये च मां नित्यं तां स्मरामि दिवानिशम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.9257)
- **Original**: ( श्रीकृष्णजन्मछण्ड 6। 52) स्त्रीपुत्रस्वजनांस्त्यक्वा. ध्यायन्ते मामहर्निशम्‌ । युष्मान्‌ विहाय तानू नित्य॑स्मराम्यहमहर्तिशम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.9258)
- **Original**: ट्रेश्ट सदा में भक्तानां ब्राह्मणानां गवामपि । क्रतूनां देवतानां च हिंसां कुर्वन्ति निश्चितम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.9259)
- **Original**: तदाउचिरं ते नश्यन्ति यथा वहाँ तृणानि च।न को5पि रक्षिता तेषां मयि हन्तर्युपस्थिते
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.9260)
- **Original**: «6 श्रीकृष्णजन्मखण्ड 6। 58--60)
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.9261)
- **Original**: 420 - संक्षिप्त ब्रह्मवैकपुराण - %555%5####अकअऋऊ अर ककऊक़ऊडऊकककडऊ अऊ अर ककअ कक अभकइकक 5 भर क अ कक ऊभ अर क/अ कफ अक अं 1 5888 8888 रहे थे। वह अग्रिशुद्ध सूक्ष्म गेरुए वस्त्रोंसे सजाया
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.9262)
- **Original**: वक्ष:स्थल उज्ज्वल दिखायी देता था। उनकी वेणी गया था। श्रेष्ठ रत्नोंके बने हुए सहस्नों कलश
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.9263)
- **Original**: प्रफुल्त मालतीकी मालाओंसे अलंकृत थी। सुन्दरी उसकी श्रीवृद्धि कर रहे थे। पारिजातपुष्पोंके हारोंसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.9264)
- **Original**: रमाका मनोहर मुख शरत्कालके चन्द्रमाकी उस विमानको सुसज्जित किया गया था। सोनेका
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.9265)
- **Original**: प्रभाको छीने लेता था। उनके भालदेशमें बना हुआ वह सुन्दर विमान अनुपम तेज:पुञ्रमय कस्तूरीबिन्दुसे युक्त सिन्दूरका तिलक शोभा दे दिखायी देता था। उससे सैकड़ों सूर्योके समान रहा था। शरत्कालके प्रफुल्ल कमलोंके समान प्रकाश फैल रहा था तथा उस विमानपर बहुत-
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.9266)
- **Original**: नेत्रोंमें मनोहर काजलकी रेखा शोभायमान थी। से श्रेष्ठ पार्षद बैठे हुए थे। उस विमानमें एक
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.9267)
- **Original**: उनके हाथमें सहस्न दलोंसे संयुक्त लीलाकमल श्यामसुन्दर कमनीय पुरुष दृष्टिगोचर हुए, जिनके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.9268)
- **Original**: सुशोभित होता था। वे अपनी ओर देखनेवाले चार हाथोंमें शल्लु, चक्र, गदा और पद्म शोभा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.9269)
- **Original**: नारायणदेवको तिरछी चितवनसे निहार रही थीं। पा रहे थे। उन श्रेष्ठ पुरुषने पीताम्बर पहन रखा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.9270)
- **Original**: पत्नियों और पार्षदोंके साथ शीघ्र ही विमानसे था। उनके मस्तकपर किरीट, कानोंमें कुण्डल
- **Translation**: 

---

