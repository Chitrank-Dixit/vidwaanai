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

### Verse 1 (Rig Ved 0.7261)
- **Original**: 3174. वेषीइस्य दूत्यं? यस्य जुजोषो अध्वरम्‌। हव्यं मर्तस्य वोछ॒हवे
- **Translation**: 

---

### Verse 2 (Rig Ved 0.7262)
- **Original**: है अग्निदेव ! आहुतियाँ ग्रहण करने के लिए आप जिस याज़क के यज्ञ को स्वीकार करते हैं, उसके हव्य को देवताओं तक पहुँचाकर दूत का कार्य भो करते हैं
- **Translation**: 

---

### Verse 3 (Rig Ved 0.7263)
- **Original**: 3175. अस्मार्क जोष्यध्वरमस्माकं॑ यज्ञमड्विर:। अस्माकं श्रृणुधी हवम्‌
- **Translation**: 

---

### Verse 4 (Rig Ved 0.7264)
- **Original**: अंड्रिरारूप हे अग्निदेव ! आप हमारे यज्ञ में हव्य को ग्रहण करें तथा हमारी स्तुति को सुनें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.7265)
- **Original**: 3176, परि ते दूरूभो रथो5स्माँ अश्नोतु विश्वत:
- **Translation**: 

---

### Verse 6 (Rig Ved 0.7266)
- **Original**: येन रक्षसि दाशुष:
- **Translation**: 

---

### Verse 7 (Rig Ved 0.7267)
- **Original**: किसी से प्रभावित न होने वाला आपका वह रथ जिससे आप (लोकहित हेतु) दान देने वालों की रक्षा करते हैं; उससे हम सबकी चारों ओर से भली-भाँति रक्षा करें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.7268)
- **Original**: [ सूक्त - 10 ] [ ऋषि - वामदेव गौतम । देवता - अग्नि । छन्द - पद पंक्ति, 4, 67 पदपंक्ति अथवा उष्णिक्‌ 5 - महापद पंक्ति 8 उष्णिक्‌ ।
- **Translation**: 

---

### Verse 9 (Rig Ved 0.7269)
- **Original**: 3177, अग्ने तमद्याश्व॑ न स्तोमे: क्रतुं न भद्रं हृदिस्पृशम्‌। ऋषध्यामा त ओहै:
- **Translation**: 

---

### Verse 10 (Rig Ved 0.7270)
- **Original**: है अग्निदेव ! आज हम याजकगण यज्ञ के समान (हितकारों) , अश्व के समान गतिशील, आपके यश को
- **Translation**: 

---

### Verse 11 (Rig Ved 0.7271)
- **Original**: 20 ऋग्वेद संहिता घाग - 2 बढ़ाने के लिए ओह नामक हृदयस्पर्शो स्तोत्रों का प्रयोग करते हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.7272)
- **Original**: 3178. अधा हवन क्रतोर्भद्रस्थ दक्षस्य साधो: । रधीरऋतस्य बृहतो बभूथ
- **Translation**: 

---

### Verse 13 (Rig Ved 0.7273)
- **Original**: है अग्निदेव ! कल्याणकारी, बलवर्द्धक, अभीष्ट प्रदान करने वाले और सत्य स्वरूप आप महान्‌ हैं तथा हमारे यज्ञ के मुख्य आधार हैं
- **Translation**: 

---

### Verse 14 (Rig Ved 0.7274)
- **Original**: 3179, एभिनों अर्कैर्भवा नो अर्वाइस्व॒र्ण ज्योति:। अग्ने विश्वेभि: सुमना अनीकै:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.7275)
- **Original**: हे अग्निदेव ! सूर्य के समान तेजस्वी, श्रेष्ठमना, आप पूज्य इद्धादि देवों के साथ हमारे यज्ञ में पधारें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.7276)
- **Original**: 3180, आभिष्टे अद्य गीर्भिगगुणन्तो5ग्ने दाशेम । प्र ते दिवो न स्तनयन्ति शुष्मा:
- **Translation**: 

---

### Verse 17 (Rig Ved 0.7277)
- **Original**: है अग्निदेव ! आज हम श्रेष्ठतम स्तोत्रों का उच्चारण करते हुए आपको प्रार्थना करते हैं। हम आपको आहुतियाँ प्रदान करते हैं । आपकी तेजस्वी लपरटें मेघसदृश ध्वनि करती हैं
- **Translation**: 

---

### Verse 18 (Rig Ved 0.7278)
- **Original**: 3181. तब स्वादिष्ठाग्ने संदृष्टिरिदा चिदह्न इृदा चिदक्तो: । श्रिये रुकमो न रोचत उपाके
- **Translation**: 

---

### Verse 19 (Rig Ved 0.7279)
- **Original**: है अग्निदेव ! आपकी प्रीतियुक्त प्रभा आभूषण के सदृश है । समस्त पदार्थों को आश्रय देने के लिए वह राक्दिन सुशोभित होती है
- **Translation**: 

---

### Verse 20 (Rig Ved 0.7280)
- **Original**: 3182 घृत न पूतं तनूररेपाः शुचि हिरण्यम्‌। तत्ते रुक्मो न रोचत स्वधाव:
- **Translation**: 

---

