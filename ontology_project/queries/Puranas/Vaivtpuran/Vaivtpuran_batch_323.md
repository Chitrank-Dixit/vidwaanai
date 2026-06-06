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

### Verse 1 (Vaivtpuran 15.6813)
- **Original**: हूँ। इसे तुम जिस-किसीको मत दे देना। इस पापयुक्त इन्द्रको जो कवच दिया था, वही अपूर्व
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.6814)
- **Original**: कवचकी कृपासे तुम्हारा रोग नष्ट हो जायगा और सूर्यकबच मैं तुमलोगोंको प्रदान करता हूँ।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.6815)
- **Original**: तुम नीरोग तथा श्रीसम्पन्न हो जाओगे-इसमें यृहस्पतिने कहा--इन्द्र! सुनो। मैं उस
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.6816)
- **Original**: संशय नहीं है। एक लाख वर्षतक हतिष्य- परम अद्भुत कबचका वर्णन करता हूँ जिसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.6817)
- **Original**: भोजनसे मनुष्यकों जो फल मिलता है, वह फल धारण करके मुनिगण पवित्र हो भारतवर्षमें
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.6818)
- **Original**: निश्चय ही इस कवचके धारणसे प्राप्त हो जाता जीवन्मुक्त हो गये। इस कवचके धारण करनेवालेके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.6819)
- **Original**: है। इस कवचको जाने बिना जो मूर्ख सूर्यकी संनिकट व्याधि भयके मारे उसी प्रकार नहीं जाती
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.6820)
- **Original**: भक्ति करता है, उसे दस लाख जप करनेपर भी है, जैसे गरुड़को देखकर साँप दूर भाग जाते हैं।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.6821)
- **Original**: मन्त्रसिद्धि नहीं प्राप्त होती। इसे अपने शिष्यको, जो गुरुभक्त और शुद्ध हो, बहाने कहा--वत्स ! इस कवचको धारण बतलाना चाहिये परंतु जो दूसरेके दुष्ट स्वभाववाले
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.6822)
- **Original**: करके सूर्यका स्तवन करनेपर तुमलोग रोग-मुक्त शिष्यको देता है, वह मृत्युको प्राप्त हो जाता है। हो जाओगे-यह निश्चित है। सूर्य-स्तवनका इस जगद्‌विलक्षण कवचके प्रजापति ऋषि हैं,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.6823)
- **Original**: वर्णन सामवेदमें हुआ है। यह व्याधिविनाशक, गायत्री छन्द है और स्वयं सूर्य देवता हैं।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.6824)
- **Original**: सर्वपापहारी, परमोत्कृष्ट, साररूप और श्री तथा व्याधिनाश तथा सौन्दर्यके लिये इसका विनियोग
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.6825)
- **Original**: आरोग्यको देनेवाला है। किया जाता है। यह सारस्वरूप कवच तत्काल, भगवन्‌! जो सनातन ब्रह्म, परमधाम, ही पवित्र करनेवाला और सम्पूर्ण पापॉका विनाशक
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.6826)
- **Original**: ज्योतीरूप, भक्तोंपर अनुग्रह करनेवाले, त्रिलोकीके है। 'हीं 37 कलीं श्रीं श्रीसूर्याय स्वाहा' मेरे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.6827)
- **Original**: नेत्ररूप, जगन्नाथ, पापनाशक, तपस्याओंके फलदाता, मस्तककी रक्षा करे। उपर्युक्त अष्टादशाक्षर-मन्त्र
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.6828)
- **Original**: पापियोंको सदा दुःखदायी, कर्मानुरूप फल प्रदान सदा मेरे कपालकों बचावे। '< हीं हीं श्री करनेवाले, कर्मके बीजस्वरूप, दयासागर, कर्मरूप, भ्रीसूर्याय स्वाहा' मेरी नासिकाकों सुरक्षित रखे।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.6829)
- **Original**: क्रियारूप, रूपरहित, कर्मबीज, ब्रह्मा, विष्णु और सूर्य मेरे नेत्रोंकी, विकर्तन पुतलियोंकी, भास्कर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.6830)
- **Original**: महेशके अंशरूप, त्रिगुणात्मक, व्याधिदाता, ओठोंकी और दिनकर दाँतोंकी रक्षा करें। प्रचण्ड
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.6831)
- **Original**: व्याधिहन्ता, शोक-मोह-भयके विनाशक, सुखदायक, मेरे गण्डस्थलका, मार्तण्ड कानोंका, मिहिर स्कन्धोंका
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.6832)
- **Original**: मोक्षदाता, साररूप, भक्तिप्रद, सम्पूर्ण कामनाओंके और पूषा जंघाओंका सदा पालन करें। रवि मेरे
- **Translation**: 

---

