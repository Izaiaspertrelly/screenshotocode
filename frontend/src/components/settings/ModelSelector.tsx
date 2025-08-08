import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../ui/select";
import { Badge } from "../ui/badge";
import { CodeGenerationModel, CODE_GENERATION_MODEL_DESCRIPTIONS } from "../../lib/models";

interface Props {
  model: CodeGenerationModel | undefined;
  setModel: (model: CodeGenerationModel) => void;
  label?: string;
  shouldDisableUpdates?: boolean;
}

function ModelSelector({
  model,
  setModel,
  label = "Model:",
  shouldDisableUpdates = false,
}: Props) {
  return (
    <div className="flex flex-col gap-y-2 justify-between text-sm">
      <div className="grid grid-cols-3 items-center gap-4">
        <span>{label}</span>
        <Select
          value={model}
          onValueChange={(value: string) => setModel(value as CodeGenerationModel)}
          disabled={shouldDisableUpdates}
        >
          <SelectTrigger className="col-span-2" id="model-selector">
            <SelectValue placeholder="Select a model">
              {model ? CODE_GENERATION_MODEL_DESCRIPTIONS[model].name : "Select a model"}
            </SelectValue>
          </SelectTrigger>
          <SelectContent>
            <SelectGroup>
              {Object.values(CodeGenerationModel).map((modelValue) => (
                <SelectItem key={modelValue} value={modelValue}>
                  <div className="flex items-center">
                    <span>{CODE_GENERATION_MODEL_DESCRIPTIONS[modelValue].name}</span>
                    {CODE_GENERATION_MODEL_DESCRIPTIONS[modelValue].inBeta && (
                      <Badge className="ml-2" variant="secondary">
                        Beta
                      </Badge>
                    )}
                  </div>
                </SelectItem>
              ))}
            </SelectGroup>
          </SelectContent>
        </Select>
      </div>
    </div>
  );
}

export default ModelSelector;
