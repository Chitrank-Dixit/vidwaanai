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

### Verse 1 (Vishnu Puran 0.9961)
- **Original**: साथ ही वुन्दावनमें विचरनेवाले घोर असुर केशीको भी आज्ञा दूँगा, जिससे वह महावली दैत्य उन्हें वहीं नष्ट कर देगा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9962)
- **Original**: अथवा [यदि किसी प्रकार बचकर] वे दोनों बसुदेव-पुत्र गोप मेरे पास आ भी गये तो उन्हें सेरा कुवल्ठयापीड़ हाथी मार डालेगा'
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9963)
- **Original**: श्रीपराइरजी बोले--ऐस। सोचकर उस दुष्टात्मा कंसने वीसखर राम और कृष्णकों मासरनेका निश्चय कर अक्रूरजीसे कहा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9964)
- **Original**: कंस उताच भो भो दानपते वाक्य क्रियतां प्रीतये मम । इतः स्थन्दनमारुह्म गम्यतां नन्दगोकुलम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9965)
- **Original**: 13 वसुदेवसुतो तत्र विष्णोरंशसमुझधवो । नाज्ञाय किल सम्धूतौ मम दुष्टो प्रवर्द्ध/:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9966)
- **Original**: 14 धनुर्महो ममाप्यत्न चतुर्दश्यां भविष्यति। आनेयौ भवता गत्वा मल्लयुद्धाय तत्र तौ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9967)
- **Original**: 15 चाणूरमुष्टिकौ मल्‍लौ नियुद्धकुछो मम। ताभ्यां सहानयोरयुद्ध सर्वलोकोउज पह्यतु
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9968)
- **Original**: 16 गजः कुबलयापीडो महामात्रप्रचोदितः । स वा हनिष्यते पापौ वसुदेवात्मजो शिशू
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9969)
- **Original**: 17 तो हत्वा बसुदेव क्व नन्दगोप॑ चर दुर्मतिम्‌। हनिष्ये पितरं॑ चैनमुग्नसेन॑ सुदुर्मतिम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9970)
- **Original**: 18 ततस्समस्तगोपानां गोश्वनान्यखिलान्यहम्‌। वित्त चापहरिष्यामि दुष्टानों मदृथ्ैषिणाम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9971)
- **Original**: 19 त्वामृते यादवाश्ैते द्विषो दानपते मम। एतेषां च वधायाह यतिष्येउनुक्रमात्तत:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9972)
- **Original**: 20 तदा निष्कण्टकं सर्व राज्यमेतदयादलम्‌ । प्रसाधिष्ये त्वया तस्मान्प््रीत्ये जीर गम्यताम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9973)
- **Original**: 29 यथा च माहिषं सर्पिर्दथि चाप्युपहार्य वे । गोपास्समानवन्तवाशु तथा वाच्यास्त्वया च ते
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9974)
- **Original**: 22 अश्रीपणशर उवाच इत्याज्ञप्तस्तदाक़ूरों महाभागवतो द्विज। प्रीतिमानभवत्कृष्णं श्रो द्रक्ष्यामीति सत्वर:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9975)
- **Original**: 23 तथेत्युक्त्वा च राजान॑ रथमारुद्दा झोभनम्‌ । श्रीविष्णुपुराण ([ अ0 1575 कंस बोल्छा--हे दानपते ! मेरी प्रसन्नताके लिये आप मेरी एक बात स्वीकार कर ल्वैजिये। यहाँसि रथपर चढ़कर आप नन्‍्दके गोकुलको जाइये
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9976)
- **Original**: वहाँ वसुदेवके विष्णुअंडासे उत्पन्न दो पूत्र हैं। मेरे नाहके हिये उत्पन्न हुए वे दुष्ट बालक वहाँ पोषित हो रहे हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9977)
- **Original**: मेरे यहाँ चतुर्दशीको धनुषयज्ञ होनेवाला है; अतः आप वहाँ जाकर उन्हें मल्लयुद्धके लिये ले आइये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9978)
- **Original**: मेरे चाणूर और मुष्ठिक नामक मल्ल युग्म-युद्धमें अति कुद्दछ हैं, [ उस थरनुर्यज्ञके दिन ] उन दोनोंके साथ मेरे इन पहल्थयानोंका ब्रन्द्रयुद्ध यहाँ सब लोग देखें
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9979)
- **Original**: अथवा महावतसे प्रेरित हुआ कुवल्यापीड नामक्त गजराज उन दोनों दुष्ट बसुदेव-पुत्र बालकोंको नष्ट कर देंगा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9980)
- **Original**: इस प्रकार उन्हें मारकर मैं दुर्मति लसुदेख, नन्‍्दगोष आर इस अपने मन्द्ति पिता उग्रंसेनको भी मार डालूँगा
- **Translation**: 

---

