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

### Verse 1 (Vishnu Puran 0.10661)
- **Original**: 27 स ल्ं प्राप्तो न सन्‍्देहों पर्त्यनामुपकारकृत्‌ । तथापि सुमहत्तेजो नाल सोदुपह तब
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10662)
- **Original**: 28 तथा हि. सजलााम्भोदनादधीरतरं तब
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10663)
- **Original**: वार्क्य नमति चैवोर्वी युष्पत्पादप्रपीडिता
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10664)
- **Original**: 29 देबासुरमहायुद्धे दैत्यसैन्यमहाभटाः । न सेहुर्पम तेजस्ते त्क्तेजो न सहाम्यहम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10665)
- **Original**: 30 संसारपतितस्पैको जन्‍्तोस्त्वे शरण परम्‌। च्रसीद त्वे प्रपन्नार्तिहर नाहाय मेडशुभम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10666)
- **Original**: 319 त्वें पयोनिधयदशौलसरितस्त्व॑ बनानि च। मेदिनी गगन खायुरापोअग्रिस्त्व॑ तथा मनः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10667)
- **Original**: 32 बुद्धिरव्याकृतप्राणा: प्राणेशस्त्व॑ तथा पुमान्‌ । पुंस: परतरे यश्च॒ व्याप्यजनमविकारबत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10668)
- **Original**: 33 झब्दादिहीनमजरममेयं॑ _क्षयवर्जितम्‌ । अवृद्धिनाओ् तट्ढह्म त्वमाद्मन्तविवर्जितम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10669)
- **Original**: 34 पश्चम अंश 3758 सो रहा था
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10670)
- **Original**: उस दुर्मति यवनने भी उस गुफामें जाकर सोये हुए राजाको कष्ण समझकर त्त्रत मारी
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10671)
- **Original**: उसके ह्मत मारनेसे उठकर राजा मुचुकुन्दने उस यवनसजको देखा। हे मैत्रेय ! उनके देखते ही ल्रह यवन उसकी क्रोघाप्रिसे जलकर भस्मीधूत हो गया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10672)
- **Original**: पूर्वकालमें राजा मुचुकुन्द देवासुर-संग्राममें गये थे; असुरोंकों मार चुकनेपर अत्यन्त निद्राल्टु होनेके कारण उन्होंने देबताओंसे बहुत समयतक सोनेक्ा बर माँगा था
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10673)
- **Original**: उस समय देवताओंने कड़ा था कि तुम्हारे जयन कसनेपर तुम्हें जो क्त्रेई जगावेगा वह तुरन्त ही अपने झरीरसे उत्पन्न हुई अप्रिसे जलकर भस्म हो जायगा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10674)
- **Original**: इस प्रकार पापी कालयवनको दग्ध कर चुकनेपर राजा मुचुकुन्दने श्रीमघुसूदनको देखकर पूछा “आप कौन हैं ?' तथ भगवानने कहा--''मैं चन्द्रबंशके अन्तर्गत यदुकुलगें वसुदेवजीके पुत्ररूपसे उत्पन्न हुआ हूँ”
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10675)
- **Original**: तब मुचुकुन्दको युद्ध गार्म्य मुनिके जचनॉक्य स्मरण हुआ। उनका स्मरण होते हो उन्होंने सर्वरूप सर्वेश्वर श्रोहरिको प्रणाम करके कहा--“हे परसेश्वर ! मैंने . आपको जान लिया है; आप साक्षात्‌ भगवान्‌ विष्णुके अंडा हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10676)
- **Original**: पूर्वकालमें गार्ग्य मुनिने कहा था कि अदट्नाईसलें युगमें द्वापरके अन्तमें यदुकुलमें श्रीह॒रिका जन्म होगा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10677)
- **Original**: निस्सन्देद्र आप भगवान्‌ किण्णुके अंश्ञ हैं और मनुष्योंके उपकारके लिये ही अवतीर्ण हुए हैं तथापि मैं आपके महान्‌ तेजको सहन करनेमें समर्थ नहीं हूँ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10678)
- **Original**: हे भगजन्‌ ! आपका शब्द सजल मेघकी घोर गर्जनाके समान अति गम्भीर है तथा आफ्के चरणोंसे पीडिता होकर पृथिवी झुकी हुई है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10679)
- **Original**: हे देव ! देवासुर-महासंमाममें दैत्य-सेनाके बड़े-बड़े योद्धागण भी मेरा तेज नहीं सड सके थे और मैं आपका तेज सहन नहीं कर सकता
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10680)
- **Original**: संसारमें पत्तित जीवॉके एकमात्र आप ही परम आश्रय हैं। है दारणागतॉका दुःख दूर करनेवाले ! आप प्रसन्न होडये और मेरे अमझ्नलोंको नष्ट कीजिये
- **Translation**: 

---

