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

### Verse 1 (Bramha 0.6401)
- **Original**: गयौ। तत्पश्चात्‌ श्रीकृष्णने पुन: महाबली मल्लराज कुशल मुष्टिक दैत्य बलदेवजीके साथ भिड़ गया।
- **Translation**: 

---

### Verse 2 (Bramha 0.6402)
- **Original**: तोशलको बायें घूँसेकी चोटसे मार गिराया। श्रीकृष्ण चाणूरके साथ परस्पर भिड़कर, नीचे
- **Translation**: 

---

### Verse 3 (Bramha 0.6403)
- **Original**: चाणूर, मुष्टिक और तोशलके मारे जानेपर शेष गिराकर, उछालकर, घुँसे और वद्धके समान
- **Translation**: 

---

### Verse 4 (Bramha 0.6404)
- **Original**: पहलवान भाग खड़े हुए। उस समय श्रीकृष्ण कोहनीसे मारकर, पैरोंसे ठोंकरें देकर तथा एक-
- **Translation**: 

---

### Verse 5 (Bramha 0.6405)
- **Original**: और बलभद्र रंगभूमिमें समवयस्क ग्वालबालोंको दूसरेके शरीरकों रगड़कर लड़ने लगे। इस तरह ! साथ ले हर्षमें भरकर उछलने-कूदने लगे। यह उन दोनोंमें बड़ा भारी युद्ध हुआ। उस युद्धमें
- **Translation**: 

---

### Verse 6 (Bramha 0.6406)
- **Original**: देख कंसको आँखें क्रोधसे लाल हो गयीं। उसने यद्यपि किसी अस्त्र-शस्त्रका प्रयोग नहीं होता
- **Translation**: 

---

### Verse 7 (Bramha 0.6407)
- **Original**: अपने सेवकोंकों आज्ञा दी, 'इन दोनों ग्वालोंको था तो भी वह अत्यन्त घोर एवं भयंकर था।
- **Translation**: 

---

### Verse 8 (Bramha 0.6408)
- **Original**: बलपूर्वक रज्जशालासे बाहर निकाल दो। पापी अपने बल और प्राणशक्तिसे ही साध्य था। ज्यों-
- **Translation**: 

---

### Verse 9 (Bramha 0.6409)
- **Original**: नन्‍्दकों भी पकड़कर तुरंत ग्रेड़ियोंमें जकड़ दो। ज्यों चाणूर श्रोहरिके साथ युद्ध करता, त्यों-ही-
- **Translation**: 

---

### Verse 10 (Bramha 0.6410)
- **Original**: बसुदेवको भी उसकी वृद्धताका विचार न रखते त्यों उसकी ग्राणशक्ति घटती जातो थी। जगन्मय
- **Translation**: 

---

### Verse 11 (Bramha 0.6411)
- **Original**: हुए कठोर दण्ड देकर मार डालो। ये जो ग्वाल- श्रीकृष्ण भी उसके साथ लीलापूर्वक युद्ध करने
- **Translation**: 

---

### Verse 12 (Bramha 0.6412)
- **Original**: बाल श्रीकृष्णके साथ उछल रहे हैं, इन सबकी लगे। वह परिश्रमसे थक गया था, अत: क्रोधपूर्वक
- **Translation**: 

---

### Verse 13 (Bramha 0.6413)
- **Original**: गौएँ छीन लो और इनके घरमें जो कुछ भी धन- श्रीकृष्णेक हाथपर हाथ मार रहा था। कंसने
- **Translation**: 

---

### Verse 14 (Bramha 0.6414)
- **Original**: सम्पत्ति हों, उसे लूट लो।' देखा, श्रीकृष्ण बल बढ़ रहा है और चाणूर, कंसको इस प्रकार आदेश देते देख भगवान्‌ धकता जा रहा है; कुपित होकर उसने याजे बंद
- **Translation**: 

---

### Verse 15 (Bramha 0.6415)
- **Original**: मधुसूदन हँस पड़े। वे उकछलकर मझपर जा चढ़े। करा दिये। इसो समय आकाशमें देवताओंके
- **Translation**: 

---

### Verse 16 (Bramha 0.6416)
- **Original**: राजाका मुकुट पृथ्वीपर गिर पड़ा। श्रोकृष्णने अनेक प्रकारके याजे बज उठे। अदृश्य भावसे
- **Translation**: 

---

### Verse 17 (Bramha 0.6417)
- **Original**: उसके केश पकड़ लिये और उसे पृथ्बीपर खड़े हुए देवता हर्षमें भरकर भगवान्‌को स्तुति
- **Translation**: 

---

### Verse 18 (Bramha 0.6418)
- **Original**: गिराकर स्वयं भी उसीपर कूद पड़े। वे सम्पूर्ण करते हुए बोले--'केशब ! चाणूर दानवको मार जगतूका भार लेकर उसके ऊपर कूदे थे, इसलिये
- **Translation**: 

---

### Verse 19 (Bramha 0.6419)
- **Original**: 308 * संक्षिप्त ब्रह्मपुराण * उसके प्राण निकल गये। उग्रसेनकुमार राजा कंस
- **Translation**: 

---

### Verse 20 (Bramha 0.6420)
- **Original**: हमारे घरमें अवतार लिया, इससे हमारा कुल संसारसे चल बसा। मरनेपर भी श्रीकृष्णने उसके
- **Translation**: 

---

