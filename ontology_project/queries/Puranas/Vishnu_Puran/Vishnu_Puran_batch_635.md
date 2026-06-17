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

### Verse 1 (Vishnu Puran 0.12681)
- **Original**: जब कि आत्मा आकाश, वायु, अग्नि, जरू और पृथिवी आदिसे सर्वधा पृथक्‌ है तो कौन बुद्धिमान्‌ व्यक्ति शरीरमें आत्मबुद्धि करेगा ?
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12682)
- **Original**: और आत्माके देहसे परे होनेपर भी देहके उपभोग्य गृह-क्षेत्रादिको कौन प्राज्ञ पुरुष “अपना' मान सकता है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12683)
- **Original**: इस प्रकार इस दारीरके अनात्पा होनेसे इससे उत्पन्न हुए पुत्र-पौत्ादिमें भी कौन विद्वान्‌ अपनापन करेगा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12684)
- **Original**: मनुष्य सारे कर्म देहके ही उपभोगके लिये करता है; किन्तु जब कि यह देह अपनेसे पृथक्‌ है, तो वे कर्म केवल बन्धन (देहोत्पत्ति) के ही कारण होते हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12685)
- **Original**: जिस प्रकार मिट्टीके घरको जल और मिट्टीसे लीपते-पोतते हैं उसी प्रकार यह पार्थिव
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12686)
- **Original**: 8 छः जश्रीविष्णुपराण
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12687)
- **Original**: तु 07 श्रीविष्णुपुराण [ अ0 7 प्॒धूतात्मकैभोंगै: पद्चभृतात्पक॑ वपु:। आप्यायते यदि ततः पुंसो भोगोउत्र कि कृत:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12688)
- **Original**: 18 अनेकजन्मसाहस्त्री संसारपदर्वी ब्रजन्‌। मोहश्रम॑ प्रयातोडसौँ वासनारेणुकुण्ठित:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12689)
- **Original**: 19 त्रक्षाल्यते यदा सोउस्प रेणुज्ञनोष्णवारिणा । तदा संसारपान्थस्य याति मोहअ्रमइशमम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12690)
- **Original**: 20 मोहश्रमे शम याते स्वस्थान्तःकरण: पुमान्‌ । अनन्यातिंशयाबार्ध परं निवार्णमृच्छति
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12691)
- **Original**: 29 निवार्णमय एवायमात्मा ज्ञानमयोउमलः । दुःखाज्ञानमया थधर्मा: प्रकृतेस्ते तु नात्मन:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12692)
- **Original**: 22 जलस्थ नाम़िसंसर्ग: स्थालीसंगात्तथापि हि । शब्दोद्रेकादिकान्धर्मास्तत्करोति यथा नृप
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12693)
- **Original**: 23 तथात्मा प्रकृतेस्सड्भादहम्मानादिदूषित: । अजते प्राकृतान्चर्मानन्‍्यस्तेभ्यो हि सोउव्ययः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12694)
- **Original**: 24 तदेतत्कथितं बीजमविद्याया मया तव। क्लेशानां च क्षयकरं योगादन्यन्न विद्यते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12695)
- **Original**: 25 रक्डिक्य उवाच त॑ तु ब्रृहि महाभाग योगं योगविदुत्तम । विज्ञातयोगशास्त्रार्थस्त्वमस्यां निभिसन्ततौ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12696)
- **Original**: 26 केशिध्वज उवाच योगस्वरूप॑ खाण्डिक्य श्रूयतां गदतो मम । यत्र स्थितो न च्यवते प्राप्य ब्रह्मलयं मुनि:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12697)
- **Original**: 27 मन एव प्रनुष्याणां कारणं बन्धमोक्षयो: । बन्धाय विषयासल्लि मुक्त्य निर्विष्य मनः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12698)
- **Original**: 28 बल कण मेगा मन कृषि विज्ञानात्मा मनो मुनि: । चिन्तयेन्पुक्तये ब्रह्मभूत॑ परेश्वरम
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12699)
- **Original**: 29 आत्पभार्व नयत्वेनं तद्ढह्म ध्यायिन मुनिम्‌। बिकार्यमात्मनश्शक्त्या लोहमाकर्षको यथा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12700)
- **Original**: 30 आत्पप्रयल्रसापेक्षा विशिष्टा या मनोगति: । तस्या ब्रह्मणि संयोगो योग इत्यभिधीयते
- **Translation**: 

---

