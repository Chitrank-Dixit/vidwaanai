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

### Verse 1 (Vishnu Puran 0.10941)
- **Original**: असधुसूदनने एक ओर रुबिमणीके और दूसरी ओर बलरामजीके भयसे कुछ भी नहीं कहा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10942)
- **Original**: तदनन्तर, ततो5निरुद्धमादाय. कृतदार॑ द्विजोत्तम । हे द्विजश्रेष्त ! यादजॉके सहित श्रीकृष्णचन्द्र सपल्नीक डद्वारकामाजगामाथ यदुचक्र चर केशव:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10943)
- **Original**: अनिरुद्धको लेकर द्वारकापुरीमें चले आये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10944)
- **Original**: --_-_--- अर “5 इति श्रीविष्णुपुराणे पह्ममेंडशेउष्टाविज्ञोौडध्याय:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10945)
- **Original**: क्ज- ऋ कम-+ उन्तीसवाँ अध्याय नरकासुरका बच श्रीपएताशर उताच श्रीपराशरजी बोले--हे मैत्रेय ! एक बार जब द्वारतत्यां स्थिते कृष्णे शक्रस्त्रिभुवनेश्वर: । श्रोभगबान्‌ द्वास्कामें हो थे त्रिभुवनपति इन्द्र अपने मत्त आजगामाथ मैत्रेय. मत्तैरावतपृष्ठगः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10946)
- **Original**: ग़जराज ऐराबतपर चढ़कर उनके पास आये
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10947)
- **Original**: द्वारकामें आकर ये भगवानसे मिले और उनसे प्रविश्य द्वारकां सो$थ समेत्य हरिणा ततः । नरकासुर्के अत्याचारोंका वर्णन किया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10948)
- **Original**: [बे कथयामास दैत्यस्थ नरकस्य विचेष्टितम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10949)
- **Original**: क>े_.. ] "है मरधुसूदत। इस समय मलुष्यसूपमें त्वया नाथेन देवानां मनुष्यत्वेषपि तिष्ठता । स्थित होकर भी आप सम्पूर्ण देजताओंके स्वामीने प्रशमं सर्वदुःखानि नीतानि मधुसूदन।। 3
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10950)
- **Original**: हमारे समस्त दुःखोंको शात्त कर दिया है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10951)
- **Original**: नपम्विव्यसनाधाय सोगष्रो घेनुकम्तथा जो अरिष्ट, धेनुक और केशी आदि असुर सर्वदा थी तपर्क्योंको क्लेघशित करते रहते थे उन सबको आपने प्रवृत्तो बस्तथा केशी ते सर्वे निहतास्वया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10952)
- **Original**: 4 मार डाला
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10953)
- **Original**: कंस, कुवल्यापीड और बालघातिनों कंस: कुबलयापीड: पूतना बालघातिनी । चूतना तथा और भी जो-जो संसारके उपद्रवरूप थे उन नाझ नीतास्त्वया सर्वे येउन्ये जगदुपद्॒बा:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10954)
- **Original**: सबको आपने नष्ट कर दिया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10955)
- **Original**: आपके बाहुदप्डकी युप्महोर्टण्डसम्धूतिपरितराते जगतलये । सत्तासे विकार हो जानेके कारण पापा दिये हुए यज्ञभागोंकों प्राप्तकर देवगण ठूप्त हो यज्वयज्ञांशसम्प्राप्या तृप्ति यान्ति दिवौकसः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10956)
- **Original**: ब्क है जनार्दन ! इस समय जिस निमित्तसे मैं सोऊहं साम्प्रतमायातो यज्निमित्त जनार्दन
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10957)
- **Original**: आपके पास उपस्थित हुआ हूँ उसे सुनकर आप उसके तच्छ्त्वा तत्पतीकारप्रयलल॑ कर्तुमरहस्ति ।। 7
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10958)
- **Original**: प्रतीकारका पयत्र करें
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10959)
- **Original**: 386 भौमो5य नरको नाम प्राग्ज्योतिषपुरेश्वर: । करोति सर्वभूतानामुपघातमरिन्दम
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10960)
- **Original**: 8 देवसिद्धासुरादीनाँ नुपाणां च जनार्दन। हत्वा तु सोउसुरः कन्या रुरुथे निजमन्दिरे
- **Translation**: 

---

