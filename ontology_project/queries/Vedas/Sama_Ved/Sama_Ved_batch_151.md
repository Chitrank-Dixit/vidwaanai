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

### Verse 1 (Sama Ved 0.3001)
- **Original**: 1163. ये सोमास: परावति ये अर्वावति सुन्विरे । ये वाद: शर्यणावति
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3002)
- **Original**: जो सोम दूरस्थ देशों में, या समीपस्थ देशों में शर्यगावत्‌ सरोत्र के निकट (उत्पन्न होते और ) संस्कारित होते हैं । (हमें इष्ट प्रदायक हों ।)
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3003)
- **Original**: [ सायण के पतानुसार 'शर्यणावत्‌' कुरुक्षेत्र के 'शर्यणा' नामक मण्डल (कपिश्नरी) की एक झील का नाप है
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3004)
- **Original**: ] 1164. य आर्जीकिषु कृत्वसु ये मध्ये पस्त्यानाम्‌ । ये वा जनेषु पद्चसु
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3005)
- **Original**: जो सोम आर्जीक देश में, कर्म करने वालों के देशों में, नदियों के किनारे या पंचजनों के बीच में उत्पन्न होता और संस्कारित किया जाता है, वह हमारे लिए सुखदायक हो
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3006)
- **Original**: [ हिलेब्राण्ट के अनुसार आर्जोक कश्मोर में एक स्थान ] 1165. ते नो वृष्टि दिवस्परि पवन्तामा सुवीर्यम्‌। स्वाना देवास इन्दव:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3007)
- **Original**: निचोड़कर निष्पादित हुआ, दीप्तिमान्‌ दिव्य सोम, हमें चुलोक से वृष्टि और उत्तम बलयुक्‍त पोषक अन्न प्रदान करे
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3008)
- **Original**: इति पदञ्ञम: खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3009)
- **Original**: षष्ठ: खण्ड:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3010)
- **Original**: 1166. आ ते वत्सोमनो यमत्परमाच्चवित्सधस्थात्‌ । अग्ने त्वां कामये गिरा
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3011)
- **Original**: हे अग्ने ! वत्स ऋषि स्तुतियों द्वागा आपसे कामना करते हैं कि आपका मन अति उच्च स्थान (ुलोक) से भी हमारे पास (सहायतार्थ) आए
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3012)
- **Original**: उत्तराचिंके अष्टमो5ध्याय: 87 1167. पुरुत्रा हि सदृड्डसि दिशो विश्वा अनु प्रभु: । समत्सु त्वा हवामड़े
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3013)
- **Original**: हे अग्ने ! आप सर्वत्र समान दृष्टि रखने वाले, सभी दिशाओं के अधिपति हैं; अत: युद्ध में अपनी सुरक्षा के निमित्त, हम आपका आवाहन करते हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3014)
- **Original**: 1168, समत्स्वग्निमवसे वाजयन्तो हवामहे। वाजेषु चित्रराधसम्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3015)
- **Original**: हम संग्राम में अपने संरक्षण के लिए, अपने बलों को प्रयुक्त करने के निमित्त, अद्भुत सामर्थ्यवान्‌ अग्नि देव का आवाहन करते हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3016)
- **Original**: 1169. त्वं न इन्द्रा भर ओजो नृग्णं शतक्रतों विचर्षणे। आ वौरं पृतनासहम्‌
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3017)
- **Original**: है शतकर्मा, विशिष्ट द्रष्टा इन््देव ! आप हमें तेजस्वितायुक्त सामर्थ्य प्रदान करें और युद्ध में शत्रुओं का नाश कर, वीरपुष्र देने वाले हों
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3018)
- **Original**: 1170. त्वं हि नः पिता वसो त्व॑ माता शतक्रतो बभूविथ । अथा ते सुम्ममीमहे
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3019)
- **Original**: है सबको आश्रय देने वाले शतकर्मा इन्द्रदेव ! आप पितातुल्य पालन करने वाले और मातातुल्य धारण करने वाले हैं। अत: हम आपके पास सुख माँगने के लिए आते हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3020)
- **Original**: 1179. त्वां शुध्पिन्युरुहूत वाजयन्तमुप ब्रुवे सहस्कृत । स नो रास्व सुवीर्यम्‌
- **Translation**: 

---

