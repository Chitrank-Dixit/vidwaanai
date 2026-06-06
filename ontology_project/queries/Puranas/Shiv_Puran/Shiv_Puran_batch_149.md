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

### Verse 1 (Shiv Puran 0.2961)
- **Original**: निर्णों गुणसंकीर्णस्तवैव गुणकेलल: । अविकायध्मकशाद्यः एक सामास्यविक्रिय:
- **Translation**: 

---

### Verse 2 (Shiv Puran 0.2962)
- **Original**: 99 4 । असाघारणकर्या च सृश्स्थितिकपक्रमात्‌। एव विधा चतुर् थ जिपत्त: पत्षंधा पुनः
- **Translation**: 

---

### Verse 3 (Shiv Puran 0.2963)
- **Original**: चतुर्थातरणे वाम्भो: पूज्ितिक्षातुगीः सह। जिवकी आज़ाका सत्कार करके मुझे मफ्रल प्रदान करें
- **Translation**: 

---

### Verse 4 (Shiv Puran 0.2964)
- **Original**: 98--106 व]
- **Translation**: 

---

### Verse 5 (Shiv Puran 0.2965)
- **Original**: 782 के संक्षिप्त विवपुएण 7 >0700750900:50594007503510350 510 05000535507470700745170475015 00405510517770305.447 54. दिवाकरपलज्ानि... दीप्ाचाब्ए्टक्क्तय:
- **Translation**: 

---

### Verse 6 (Shiv Puran 0.2966)
- **Original**: आदित्यो भास्करों भानू रसिल्ेस्यनुपूर्बशा:। अ्कों ज्रह्या तथा राष्ट्रों विष्णुआदित्पमूर्तयः
- **Translation**: 

---

### Verse 7 (Shiv Puran 0.2967)
- **Original**: विस्तत सुतत योधिन्याप्यापिन्यपरा: घुऊ। उपा प्रझा सथा प्राज्ञा संध्या चेत्यपि शक्तत:
- **Translation**: 

---

### Verse 8 (Shiv Puran 0.2968)
- **Original**: स्फ्कृत्य स्पेमादिकेतुफयला प्रद्ाक्ष शिल्घायिता: दिकषयोराज्षया नुप्ना मद्भले प्रदिशन्तु पे
- **Translation**: 

---

### Verse 9 (Shiv Puran 0.2969)
- **Original**: अंथ का दादशादित्यास्तथा इाटस शक्तय:। ऋषपो देवराजर्या: पत्रगापरसों गणाः
- **Translation**: 

---

### Verse 10 (Shiv Puran 0.2970)
- **Original**: ऋमण्यश् तथा यक्षा राक्षसाक्ष सुर्तया। सा सप्तगणाओते सप्तच्छन्दोमपा हयोाः
- **Translation**: 

---

### Verse 11 (Shiv Puran 0.2971)
- **Original**: वाल्ाशित्यादपद्नैंध. सर्वे. झिजफ्टार्सयतः: । सत्कृत्य जिवपोराज्ौ मद्जले प्रदिवानु ये
- **Translation**: 

---

### Verse 12 (Shiv Puran 0.2972)
- **Original**: सूर्यदियसे सम्बन्ध रखनेवाले छडों अड्न, भास्कर, भानु, रति, अर्क, ब्रह्मा, रूद्ध सथा विष्णु--ये आठ आदित्यमूर्तियाँ और उनकी विस्तरा, सुतरा, जोधिनी, आप्यायिनों तथा उनके अतिरिक्त उषा, श्रभा, प्राज्ञा और संध्या--थे शाक्तियाँ;: चनद्भमासे लेकर केतुपर्थन्त शिवभावित ग्रह, बारह आदित्य, उनकी यारह दाक्तियाँ तथा ऋषि, देवता, गन्धर्ध, नाग, अप्सराओंके समूह, प्रामणी गण, सात छत्दोमय अश्न, करनेवाले हैं। थे स्लेग शिव और पार्वतीकी आज़ाका आदर करते हुए मुझे मजूरठ प्रदान करें
- **Translation**: 

---

### Verse 13 (Shiv Puran 0.2973)
- **Original**: 102--6108
- **Translation**: 

---

### Verse 14 (Shiv Puran 0.2974)
- **Original**: अऋषण्य देघदेवस्प मुर्तिर्भूमष्डलाधिप: । अतुःबष्टिएएश्यों. शुद्धितत्वे. अलिष्ितः
- **Translation**: 

---

### Verse 15 (Shiv Puran 0.2975)
- **Original**: मिर्तुणों गुणसंक्रीजस्तकैव गुणकेखर: अविफारत्मकों देजहहतः साधारण: पुर
- **Translation**: 

---

### Verse 16 (Shiv Puran 0.2976)
- **Original**: असाधारणकर्मा च सु्टिस्थितिल्यक्रमात्‌ ! एवं ज्रिधा उतुर्सा च विधक्त: पनञ्नघा पुनः
- **Translation**: 

---

### Verse 17 (Shiv Puran 0.2977)
- **Original**: विवप्रिय: कियासक्त: शिवफाटार्चने रतः
- **Translation**: 

---

### Verse 18 (Shiv Puran 0.2978)
- **Original**: 006] 38 किन । ्् न्‍ £ ई
- **Translation**: 

---

### Verse 19 (Shiv Puran 0.2979)
- **Original**: सनातन, दक्ष आदि त्रह्मपुत्र, ग्यारह प्रजापति
- **Translation**: 

---

### Verse 20 (Shiv Puran 0.2980)
- **Original**: * वायथीयसेटहिता * क8के ##₹0%0 7 701/7777 5744. 4 4 4 4 5 $# 77 2; 0 *'
- **Translation**: 

---

