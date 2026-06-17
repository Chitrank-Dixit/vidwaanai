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

### Verse 1 (Vamanpuran 0.1121)
- **Original**: 60 पारा चर्मण्वती लूपी विदिशा बेणुमत्यपि। सिप्रा हावन्ती च तथा पारियात्राश्रया: स्मृता:
- **Translation**: 

---

### Verse 2 (Vamanpuran 0.1122)
- **Original**: 24 शोणो महानदश्लैब नर्मदा सुरसा कृपा। मन्दाकिनी दशार्णा च॒ चित्रकूटापवाहिका
- **Translation**: 

---

### Verse 3 (Vamanpuran 0.1123)
- **Original**: 25 चित्रोत्पला वै तमसा करमोदा पिशाचिका। तथान्या पिप्पलश्रोणी विपाशा वद्जुलावती
- **Translation**: 

---

### Verse 4 (Vamanpuran 0.1124)
- **Original**: 26 सत्सन्तजा शुक्तिमती मज्निष्ठा कृत्तिमा बसु:। ऋक्षपादप्रसूता चर तथान्या बालुबाहिनी
- **Translation**: 

---

### Verse 5 (Vamanpuran 0.1125)
- **Original**: 27 शिवा पयोष्णी निर्विन्ध्या तापी सनिषधावती
- **Translation**: 

---

### Verse 6 (Vamanpuran 0.1126)
- **Original**: वेणा वैतरणी चैव सिनीबाहु: कुमुद्गती
- **Translation**: 

---

### Verse 7 (Vamanpuran 0.1127)
- **Original**: 28 तोया चैब महागौरी दुर्गन्‍्धा वाशिला तथा। विन्ध्यपादप्रसूताश्च नद्यः पुण्यजला: शुभा:
- **Translation**: 

---

### Verse 8 (Vamanpuran 0.1128)
- **Original**: 29 गोदावरी भीमरथी कृष्णा वेणा सरस्वती। तुड्डभद्रा सुप्रयोगा बाह्मा कावेरिरिव च
- **Translation**: 

---

### Verse 9 (Vamanpuran 0.1129)
- **Original**: 30 दुग्धोदा नलिनी रेवा वारिसेना कलस्वना। एतास्त्वपि महानद्य: सहापादविनिर्गता:
- **Translation**: 

---

### Verse 10 (Vamanpuran 0.1130)
- **Original**: 31 कृतमाला ताप्रपर्णी बद्ुला चोत्पलावती। सिनी चैव सुदामा च शुक्तिमत्प्रभवास्त्विमा:
- **Translation**: 

---

### Verse 11 (Vamanpuran 0.1131)
- **Original**: 32 सर्वा: पुण्या: सरस्वत्य: पापप्रशमनास्तथा। जगतो मातरः सर्वा: सर्वा: सागरयोपषितः
- **Translation**: 

---

### Verse 12 (Vamanpuran 0.1132)
- **Original**: 33 अन्या: सहस््रशश्षात्र क्षुद्रनद्यो हि राक्षस। सदाकालबहाश्चान्या: प्रावृदूकालवहास्तथा। उद्ड्मध्योद्धवा देशा: पिबन्ति स्वेच्छया शुभा:
- **Translation**: 

---

### Verse 13 (Vamanpuran 0.1133)
- **Original**: 34 कुशट्टा: पाकझ्ालकाश्या:. सह कोसलाभि:
- **Translation**: 

---

### Verse 14 (Vamanpuran 0.1134)
- **Original**: 35 बुका: शबरकौवीरा: सभूलिड्रा जनास्त्विमे। शकाश्ैव समशका मध्यदेश्या जनास्त्विमे
- **Translation**: 

---

### Verse 15 (Vamanpuran 0.1135)
- **Original**: 36 वाह्वीका वाटथानाश्व आभीरा: कालतोयका:। अपरान्तास्तथा शुद्ा : पहवाश्च सखेटकाः
- **Translation**: 

---

### Verse 16 (Vamanpuran 0.1136)
- **Original**: 37 गान्धारा सिन्धुसौवीरमद्रका: । शातद्रवा ललित्थाश्ष पारावतसमूषका:
- **Translation**: 

---

### Verse 17 (Vamanpuran 0.1137)
- **Original**: 38 मापरोबवायासब कैकेया दशमास्तणा । क्षत्रिया: प्रातिवैश्याश्न वैश्वशूद्रकुलानि च
- **Translation**: 

---

### Verse 18 (Vamanpuran 0.1138)
- **Original**: 39 काम्बोजा दरदाओव बर्बरा हाडुलौकिका:। चीनाओैव तुषाराश्न बहुधा बाह्यतोदरा:
- **Translation**: 

---

### Verse 19 (Vamanpuran 0.1139)
- **Original**: 40 आत्रेया: सभरद्वाजा: प्रस्थलाश्न दशेरकाः। लम्पकास्ताबका रामा: शूलिकास्तड्रणै: सह
- **Translation**: 

---

### Verse 20 (Vamanpuran 0.1140)
- **Original**: 49 * श्रीवामनपुराण * [ अध्याय 13 बेणुमती, सिप्रा तथा अवन्ती--ये नदियाँ पारियात्र- पर्वतसे निकली हुई हैं। महानद, शोण, नर्मदा, सुरसा, कृपा, मन्दाकिनी, दशार्णा, चित्रकूटा, अपवाहिका, चित्रोत्पला, तमसा, करमोदा, पिशाचिका, पिप्पलश्रोणी, विपाशा, वज्जुलावती, सत्सन्तजा, शुक्तिमती, मज्िप्ठा, कृत्तिमा, बसु और बालुवाहिनी --ये नदियाँ तथा दूसरी जो बालुका बहानेवाली हैं, ऋक्षपर्वतकी तलहटीसे निकली हुई हैं
- **Translation**: 

---

