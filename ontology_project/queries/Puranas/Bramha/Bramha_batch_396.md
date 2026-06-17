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

### Verse 1 (Bramha 0.7901)
- **Original**: अग्निहोत्री और यज्ञकर्ता होते हुए भी शुद्रोचित वह ब्राह्मणत्वसे भ्रष्ट होकर क्षत्रिययोनिमें जन्म
- **Translation**: 

---

### Verse 2 (Bramha 0.7902)
- **Original**: गतिको प्राप्त होता है। पेटमें शूद्रान्न शेष रहनेके लेता है। जो विप्र लोभ और मोहका आश्रय ले
- **Translation**: 

---

### Verse 3 (Bramha 0.7903)
- **Original**: कारण वह ब्रह्मलोकसे भ्रष्ट हो जाता है। शुद्रान्न- अपनी मन्द बुद्धिके कारण दुर्लभ ब्राह्मणत्वको
- **Translation**: 

---

### Verse 4 (Bramha 0.7904)
- **Original**: भोजी ब्राह्मण शूद्॒त्वको प्राप्त होता है--इसमें पाकर भी सदा वैश्यकर्मका अनुष्ठान करता है,
- **Translation**: 

---

### Verse 5 (Bramha 0.7905)
- **Original**: अन्यथा बिचारके लिये स्थान नहीं है।
- **Translation**: 

---

### Verse 6 (Bramha 0.7906)
- **Original**: ब्राह्मण वह वैश्ययोनिको प्राप्त होता है; अथवा यदि बैश्य
- **Translation**: 

---

### Verse 7 (Bramha 0.7907)
- **Original**: अपने उदरमें जिसका अन्न शेष रहते प्राण-त्याग * यस्तु शूद्र: स्थधर्मेण ज्ञानविज्ञानवाज्शुत्रि:। धर्मज्ञो धर्मनित: स धर्मफलमस्वुतेआ
- **Translation**: 

---

### Verse 8 (Bramha 0.7908)
- **Original**: रा (223। 21)
- **Translation**: 

---

### Verse 9 (Bramha 0.7909)
- **Original**: तेन शुद्रान्‍्रशेषेण. ब्रह्मस्थानादपाकृत:। ब्राह्मण: शूद्रतामेति नास्ति तन्न बिचारणा
- **Translation**: 

---

### Verse 10 (Bramha 0.7910)
- **Original**: (223। 26) हैं, कैसे ब्राह्मणभावको प्राप्त हो सकते हैं? शिवजी बोले--देवि ! भ्राह्मणत्वकी प्राप्ति अत्यन्त
- **Translation**: 

---

### Verse 11 (Bramha 0.7911)
- **Original**: » उच्च चर्णकी अधोगति और नीच यर्णकी ऊर्घ्वातिका कारण « 379 00,332 752 550007 नस नब 0 _ 30-57: 57777 77: >> €ऋऋ छऋगण!
- **Translation**: 

---

### Verse 12 (Bramha 0.7912)
- **Original**: ौूएऑ स्ससूननन करता है और जिसके अन्नसे जीवन-निर्वाह करता
- **Translation**: 

---

### Verse 13 (Bramha 0.7913)
- **Original**: क्षत्रियरूपमें उत्पन्न होनेपर वह जन्मसे हो अच्छे है, उसीकी योनिको प्राप्त होता है। जो लोग दुर्लभ
- **Translation**: 

---

### Verse 14 (Bramha 0.7914)
- **Original**: संस्कारका होता है। उपनयनके पश्चात्‌ ब्रह्मचर्यव्रतके ब्राह्मणत्वको अनायास ही पाकर उसकी अवहेलना
- **Translation**: 

---

### Verse 15 (Bramha 0.7915)
- **Original**: पालनमें तत्पर हो बह संस्कारसम्पन्न द्विज होता है। करते हैं अथवा अभक्ष्य-भक्षण करते हैं, बे
- **Translation**: 

---

### Verse 16 (Bramha 0.7916)
- **Original**: यह समय-समयपर दान देता, प्रचुर दक्षिणा देकर श्राह्मणत्वसे गिर जाते हैं। शराबी, ब्रह्महत्यारा, चोर, । वैभवपूर्ण यज्ञ करता और वेदाध्ययन करके स्वर्गकी ब्रत भड़ करनेवाला, अपवित्र, स्वाध्याय न करनेवाला,
- **Translation**: 

---

### Verse 17 (Bramha 0.7917)
- **Original**: इच्छासे आहबनीय आदि तीनों अग्नियोंकी सदा पापी, लोभी, अपकारी, शठ, त्रतहीन, शूद्रीका पति,
- **Translation**: 

---

### Verse 18 (Bramha 0.7918)
- **Original**: उपासना करता है। राजा होनेपर वह संकल्पके दोगलेका अन्न खानेबाला, सोमरस बेचनेवाला और
- **Translation**: 

---

### Verse 19 (Bramha 0.7919)
- **Original**: जलसे भीगे हाथोंद्वारा दान देता और सदा धर्मपूर्वक नीचसेवी ब्राह्मण ब्राह्मणत्वसे भ्रष्ट हो जाता है।' प्रजाका पालन करता है। स्वयं सत्यवादी होकर सदा गुरुस्त्रीगामी, गुरुद्वेषी, गुरुनिन्दापरायण तथा ब्रह्मद्ठोहो
- **Translation**: 

---

### Verse 20 (Bramha 0.7920)
- **Original**: सत्यका ही अनुष्ठान करता है, शुद्धिपर दृष्टि रखता ब्राह्मण भी ब्रह्मयोनिसे गिर जाता है। है और धर्मंदण्डसे युक्त हो धर्म, अर्थ एवं कामरूप जो शूद्र सब कर्म शास्त्रीय विधिके अनुसार
- **Translation**: 

---

