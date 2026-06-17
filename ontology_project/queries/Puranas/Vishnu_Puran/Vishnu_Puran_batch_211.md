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

### Verse 1 (Vishnu Puran 0.4201)
- **Original**: जब कोई उससे बहुत पूछताछ करता तो जडके समान कुछ असंस्कृत, असार एवँ ग्रामीण वाक्योंसे मिले हुए वचन बोल देता
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4202)
- **Original**: निरन्तर मैला-कुचैला जरीर, मलिन बस्तर और अपरिमार्जित दन्तयुक्त रहनेके कारण वह ब्राह्मण सदा अपने नगरनित्रासियोंसे अपमानित होता रहता था
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4203)
- **Original**: हे मैत्रेय ! योगश्रीके लिये सबसे अधिक हानिकारक
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4204)
- **Original**: 170 श्रीविष्णुपुराण ( अ* 13 जूक बनानल्यतमकेसुकत रे वे योगी सता । वह शीघ्र ही सिद्धि लाभ कर लेता है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4205)
- **Original**: अतः जना
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4206)
- **Original**: योगीको, आस दांत न करते हुए ऐस आचरण करना चाहिये जिससे स्लरेग अपमान र संगतिसे दूर हिरण्यगर्भवचन॑ विचिन्त्येत्थ॑महामतिः । रहें
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4207)
- **Original**: हिरण्यगर्भके इस सारयुक्त बचनफों स्मरण आत्मानं दर्शवामास जडोन्मत्ताकृति जने
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4208)
- **Original**: रखते हुए वे महामति विप्रवर अपने-आपको लोगॉमें जड़ भुुद्कक्ते कुल्माषब्रीज्ञादिशाकं वन्य फल कणान्‌ । और उन्पत्त-सा ही प्रकट करते थे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4209)
- **Original**: कुल्माष (जौ यदश्यटाप्राति
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4210)
- **Original**: आदि) धान, श्ञाक, जैगली फल अथवा कण आदि जो ति सुबहु तदते कालसंयमम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4211)
- **Original**: 45 कुछ भश्ष्य मिल जाता उस थोड़ेसेको भी बहुत मानकर वे पितर्युपरते स्रोइथ भ्रातृभ्रातृव्यबान्धवैः । उसीको खा लेते और अपना कालक्षेप करते रहते
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4212)
- **Original**: कारित: क्षेत्रकर्माद कदन्नाहारपोषितः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4213)
- **Original**: फिर पिताके शान्त हो जानेपर उनके भाई-बन्धु उनका सतूक्षपीनाबयत्रों जड़कारी चर कर्मणि सड़े-गले अन्नसे पोषण करते हुए उनसे खेती-बारीका सर्वलोकोपकरणं च बभूयाहारवेतन: ! कार्य कराने लगे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4214)
- **Original**: वे बैलके समान पुष्ट शरीरवाले सर्वल्लेकोपकरणं.. बभूवाहारबेतन:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4215)
- **Original**: और कर्ममें जडवत्‌ निश्वेष्ट ये । अतः केवल आहारमात्रसे त॑ तादृशमसंस्कारं॑ विप्राकृतिविचेष्टितम्‌। ही वे सब ल्मेगोंके यन्‍्ल बन जाते थे। [ अर्थात्‌ सभी क्षत्ता पृषतराजस्य काल्ये पशुमकल्पयत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4216)
- **Original**: ल्मेग उन्हें आहारमात्न देकर अपना-अपना काम निकाल छिया करते थे ]
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4217)
- **Original**: रात्रौ ते समलक्कृत्य वैशसस्थ विधानत: । जोगेशर उन्हें इस प्रकार संस्कारशून्य और ब्राह्मणवेषके विरुद्ध अधिष्टित॑ महाकाली ज्ञात्वा योगेश्वरं तथा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4218)
- **Original**: आचरणवाल्म देख रात्रिके समय पृषतराजके सेवकोने ततः खडडड समादाय निशितं निश्चि सा तथा । श्रक्तिकी विधिसे सुसज्जितकर कालीका बलिपशु बनाया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4219)
- **Original**: कर क्र्रकर्माणमच्छिनत्कण्ठमूलत:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4220)
- **Original**: कि इस प्रकार एक परमयोगीश्वत्को बलिके लिये देवी पपौ रुधिरमुल्बणम्‌ उपस्थित देख महाकाल्जने एक ती क्षण खड़ड ले उस क्र्रकर्मा स्वपार्षदयुता मुल्न्रणम्‌
- **Translation**: 

---

