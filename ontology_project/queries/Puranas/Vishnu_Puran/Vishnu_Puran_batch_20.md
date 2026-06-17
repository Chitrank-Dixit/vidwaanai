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

### Verse 1 (Vishnu Puran 0.381)
- **Original**: फिर उन अनादि पसमेश्वरने पृथियीकों समतऊ कर उसपर जहाँ-तहाँ पर्वतोंकों विभाग करके स्थापित कर दिया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.382)
- **Original**: सल्यसंकल्प भगवानने अपने अमोघ प्रभावरों पूर्वकल्पके अन्तमें दग्ध हुए समस्त पर्वतोंको पृथिवी-तकलपर यथास्थान रच दिया।48। तदनन्तर उन्होंने सप्तद्रीपादि-क्रमसे पृथिवीका यथायोग्य विभाग कर भूलॉकार्दि चारों लोकोंकी पूर्ववत्‌ कल्पना कर दी
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.383)
- **Original**: फिर उन भश्वान्‌ हरिने रजोगुणसे युक्त हो ऋतुर्मुस्रघारो ऋष्मारूप धारण कर सृश्टिकों रचना की
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.384)
- **Original**: सूष्टिको रचनायें भगवान्‌ ते केवऊ निभित्तमान ही हैं, क्योंकि उसकी प्रधान कारण तो सृज्य पदार्थोंकी शक्तियाँ ही हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.385)
- **Original**: हे तपस्वियोमें श्रेष्ट मैत्रेय ! यस्तुओकी रचनामें निमित्तमान्रको छोड़कर और किसी बातज्यी आवश्यकता भो नहों है, क्योंकि वस्तु तो अपनी हो [परिणाम] गक्तिसे यस्तुता (स्थूलरूपता) को प्राप्त हो जाती है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.386)
- **Original**: अं पर सननन+ इति आीविष्णुपुणणे प्रथमें$े चतुर्थो$घ्यायः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.387)
- **Original**: ञजत+ हऔ नचनन
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.388)
- **Original**: आ्‌5 ] श्रथम अंश श्5 पाँचवाँ अध्याय अविद्यादि विविध सर्गोका वर्णन श्रीमैत्रेय उदाच अपैच्नेयजी वोले--हे द्विजराज! सर्गक आदियें यथा ससर्ज देवोडसों देवर्पिपितुदानवान । भगवान्‌ ब्रह्माजीने पृथिवी, आकाझ और जल आदियें रहनेवाले मनुष्यतिर्यग्वृक्षादीन्‍्भृव्योमसलिलौकस:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.389)
- **Original**: 9 यदुर्ण यत्स्वभाव॑ च॒ यद्र॒ुप॑ च जगदद्विज । सर्गांदौ सृष्टवान्त्रह्मा तत्ममाचक्ष्य कृत्खश:ः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.390)
- **Original**: 2 अऔपराशर उवाच मैत्रेय कथवाम्येतच्छृणुष्च॒सुसमाहितः । यथा ससर्ज देवोउसौ देवादीनखिलान्विभु:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.391)
- **Original**: 3 सृष्टि चिन्तयतस्तस्य कल्पादिषु यथा पुरा ! अबुद्धिपूर्वक: सर्ग: प्रादुर्भूतस्तमोमय:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.392)
- **Original**: 4 तमो मोहो महामोहस्तामिस्रो हान्धसंज्ञितः । अविद्या पद्ञपर्वषा प्रादुर्भूता महात्ममः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.393)
- **Original**: 5 पश्नधाउवस्थितः सर्गो ध्यायतो5प्रतिबोधवान्‌ । बहिरन्तोउप्रकाशश्न संवृतात्मा नगात्मक:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.394)
- **Original**: 6 मुख्या नगा यतः प्रोक्ता मुख्यसर्गस्ततस्त्ववम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.395)
- **Original**: 7 त॑ दृष्टठाउसाधक सर्गममन्यदपरं पुनः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.396)
- **Original**: 8 तस्थाभिध्यायतः सर्गस्तिर्यकुल्लोताभ्यवर्त्तत । यस्मात्तियकृप्रवृत्तिस्स तिर्यकस्नोतास्तत: स्पृत:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.397)
- **Original**: 9 पश्चादयस्ते विख्यातास्तप: प्राया हावेदिन: । उत्पथग्राहिणश्लैव॒तेउज्ञाने ज्ञानमानिन:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.398)
- **Original**: 10 अहडइकृता अहम्माना अष्ट्राबिंशद्रधात्मका: । देव, ऋषि, प्ितृगण, दानव, मनुष्य, तिर्यक्‌ और वृक्षादिकों जिस प्रकार रचा तथा जैसे गुण, स्वभाव और रूपवाले जगत्‌की रचना की यह सब आप मुझसे कहिये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.399)
- **Original**: श्रीपराशरजी खोले--हे सैत्रेय ! भगवान्‌ विभुने जिस प्रकार इस सर्गकी रचना की वह मैं तुमसे कहता हूँ; सावधान होकर सुनो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.400)
- **Original**: सांकि आदियमें ब्रह्माजीके पूर्ववत्‌ सृष्टिका चिन्तन करनेपर पहले अबुद्धिपूर्वक [अर्थात्‌ पहले-पहल असावधानी हो जानेसे)] तमोगुणी सुष्टिका आविर्भाव हुआ
- **Translation**: 

---

