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

### Verse 1 (Rig Ved 0.11021)
- **Original**: हे गोपते इन्द्रदेव ! आप बहुत. सी गौएँ एवं घोड़े प्रदान करके हमारे इच्छाओं की पूर्ति करें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.11022)
- **Original**: 4793. तद्गों गाय सुते सचा पुरुहृताय सत्वने
- **Translation**: 

---

### Verse 3 (Rig Ved 0.11023)
- **Original**: शं यदगवे न शाकिने
- **Translation**: 

---

### Verse 4 (Rig Ved 0.11024)
- **Original**: हे स्तुतिरत स्तोताओ ! आप शत्रु को जीतने वाले इद्धदेव का यशोगान करें । जैसे गाय उत्तम घास से प्रसत्र होती है, वैसे हो तैयार सोम सहित स्तुति से इद्धदेय सुख पाते हैं
- **Translation**: 

---

### Verse 5 (Rig Ved 0.11025)
- **Original**: 4794. न घा बसुर्नि यमते दानं वाजस्य गोमत: । यत्सीमुप श्रवद्गिर:
- **Translation**: 

---

### Verse 6 (Rig Ved 0.11026)
- **Original**: सभी के आश्रयदाता वे इद्धदेव हमारी स्तुतियों को सुनने के बाद हमें धन-धान्य के रूप में अपार वैभव देने से नहीं रुकते हैं
- **Translation**: 

---

### Verse 7 (Rig Ved 0.11027)
- **Original**: 4795, कुवित्सस्य प्र हि बर्ज गोमन्तं दस्युहा गमत्‌। शचीभिरप नो बरत्‌
- **Translation**: 

---

### Verse 8 (Rig Ved 0.11028)
- **Original**: है इद्धदेव ! हिंसा करने वालों, गोशाला से गौएँ चुराने और उन्हें छिपा देने बालों को आप शीघ्रता से ढूँढ़ कर दण्डित करें और गौओं को मुक्त कराएँ
- **Translation**: 

---

### Verse 9 (Rig Ved 0.11029)
- **Original**: 4796. इमा 3 त्वा शतक्रतो5भि प्र णोनुवुर्गिर: । इन्द्र वत्सं न मातर:
- **Translation**: 

---

### Verse 10 (Rig Ved 0.11030)
- **Original**: है इन्द्रदेव
- **Translation**: 

---

### Verse 11 (Rig Ved 0.11031)
- **Original**: गौएँ जिस तरह बछड़ों कौ पुकार पर उनकी ओर भागतो हैं, वैसे ही वे स्तुतियाँ आपकी ओर हो गमन करती हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.11032)
- **Original**: 4797, दृणाशं सख्यं तव गौरसि बीर गव्यते। अश्नो अश्वायते भव
- **Translation**: 

---

### Verse 13 (Rig Ved 0.11033)
- **Original**: हे इद्धदेव ! आप गाय एवं घोड़ों को इच्छा करने बालों की इच्छा को पूर्ण करते हैं। आपकी मित्रता कभी नष्ट नहीं होती है
- **Translation**: 

---

### Verse 14 (Rig Ved 0.11034)
- **Original**: 60 ऋग्वेद संहिता भाग - 2 4798. स मन्दस्वा हान्धसो राधसे तन्वा महे । न स्तोतारं निदे कर:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.11035)
- **Original**: हे इन्द्रदेव (आप अपने लिए प्रदत्त अन्नरूप सोम से हषट-पुष्ट हों । स्तोताओं को निन्दक के अधीन न होने दें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.11036)
- **Original**: 4799. इमा उ त्वा सुतेसुते नक्षन्ते गिर्वणो गिर:
- **Translation**: 

---

### Verse 17 (Rig Ved 0.11037)
- **Original**: वत्सं गायो न घेनवः
- **Translation**: 

---

### Verse 18 (Rig Ved 0.11038)
- **Original**: हे स्तुत्य इन्द्रदेव ! जिस प्रकार दुधारू गौएँ बछड़ों के पास स्वयं ही जा पहुँचती हैं, उसी प्रकार सोम निष्पादन के समय स्तुतियाँ आपके पास स्वतः पहुँचती हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.11039)
- **Original**: 4800, पुरूतम॑ पुरूणां स्तोतृणां विवाचि। वाजेभिवाजयताम्‌
- **Translation**: 

---

### Verse 20 (Rig Ved 0.11040)
- **Original**: हमारी श्रेष्ठतम स्तुतियाँ आपको प्राप्त होती हैं । हविष्यात्र के साथ (संयुक्त होकर) वे आपको बलवान्‌ बनायें
- **Translation**: 

---

