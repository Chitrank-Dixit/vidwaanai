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

### Verse 1 (Vishnu Puran 0.7941)
- **Original**: बल- सत्यावल्तेकनात्कृष्णो5प्यात्मानं॑ गोचक्रान्तरावः स्थितमिव मेने
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7942)
- **Original**: सकलयादवसमक्ष॑ चाक़ूरमाह
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7943)
- **Original**: एतद्धि मणिरत्रमात्य- संशोधनाय एतेषां यदूनां मया दर्शितम एतथ् मम बलभद्रगस्य च॒ सामान्य पितृधन चैतत्सत्यभामाया नान्यस्थैतत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7944)
- **Original**: एतच्च सर्वकालं शुचिना ब्रह्मचर्यादिगुणबता प्रियमाणमशेषराष्ट्र स्योपकासरकमशुचिना प्रियमाणमाधारमेव हन्ति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7945)
- **Original**: अतोजहमस्य षोडशस््रीसहस्र- परिग्रहादसमर्थो. धारणे कथमेतत्सत्यभामा स्वीकरोति
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7946)
- **Original**: आर्यबलभद्रेणापि मदिरापानाद्यशेषोषभोगपरित्याग: कार्य:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7947)
- **Original**: तदले यदुत्जेको5य बलभद्गः अहं चल सत्या च त्वां दानपते प्रार्थवाम:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7948)
- **Original**: तद्भवानेव धारयितुं समर्थ:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7949)
- **Original**: त्वदूधू्त चास्य॒राष्ट्रस्योपकारक॑ तद्भवानशेषराष्ट्रनिमित्त- मेतत्पूर्ववद्धारयत्वन्यन्न वक्तव्यमित्युक्तो दानपतिस्तथेत्याह जग्राह च तन्यहारत्रम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7950)
- **Original**: ततः प्रभृत्यक्रूर: प्रकटेनैव तेनाति: जाज्वल्यमानेनात्मकण्ठावसक्तेनादित्य इबांशुमाली चार
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7951)
- **Original**: इत्येतद्धशभवतो मिथ्याभिज्वस्तिक्षाऊून॑ यः स्मरति न तस्य कदाचिदल्पापि मिथ्याभिश्स्ति- भंवति अव्याहताखिलेन्द्रियश्लाखिल्त्पापमो क्ष- मवाप्लोति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7952)
- **Original**: तब अक्रूस्जीने कहा, ''मुझे यह मणि हतथन्‍्वाने दो थी, यह जिसकी हो बह़ ले ले
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7953)
- **Original**: उसको देखनेपर सभी यादवोंका विस्मयपुर्वक साधु, साधु' यह बचन सुना गया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7954)
- **Original**: उसे देखकर बलभद्रजोने ' अच्युत्के ही समान इसपर मेगा भी अधिकार है' इस प्रकार अपनी अधिक स्पा दिखलाई
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7955)
- **Original**: तथा “यह मेरी ही पैक़क सम्पत्ति है' इस तरह सत्य- भामाने भी उसके लिये अपनी उल्कट अभिलाषा प्रकट को
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7956)
- **Original**: बलभद्र और सत्यभामाको देखकर कृष्ण- चन्द्रने अपनेको बैऊ और पहियेके बीचमें पड़े हुए जीवके समान दोनों ओरसे संकटग्रस्त देखा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7957)
- **Original**: और समस्त यादयोंके सामने ये अक्ररजीसे बोले
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7958)
- **Original**: “इस मणिरत्रको मैंने अपनी सफाई देनेके ल्क्यि हो इन यादल्रोंक दिखवाया था। इस मणिपर मेश और खत्ठभद्रजीका तो समान अधिकार है और सत्यभामाकों यह पैतृक सम्पत्ति है; और किसीका इसपर कोई अधिकार नहीं है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7959)
- **Original**: बह मणि सदा शुद्ध और बहाचर्य आदि गुणयुक्त रहकर धारण करनेसे सम्पूर्ण गहुक्ता हित करती है और अज्लुद्धावस्थामें घारण करनेसे अपने आश्रयदाताकों भी मार डालती है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7960)
- **Original**: मेरे सोलह हजार स्तरियाँ हैं, इसलिये मैं इसके धारण करनेमें समर्थ नहीँ हूँ, इसीलिये सत्यभामा भी इसको कैसे धारण कर सकती है?
- **Translation**: 

---

